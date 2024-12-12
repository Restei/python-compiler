
from collections import deque 
import webbrowser
unique_id = 0

class Node:
    """
    Classe représentant un nœud dans l'arbre syntaxique.
    """

    def __init__(self,name,father= None):
        """
        Initialise un nœud avec un nom et un identifiant unique.

        :param name: Nom du nœud (représentant la règle ou le contenu syntaxique).
        """

        global unique_id
        self.id = unique_id 
        self.name = name
        self.succ = []
        self.brother = None
        self.father = father
        unique_id+=1

    def __repr__(self):
        return self.name
    
    def __getitem__(self,i):
        return self.succ[i]

    def __contains__(self,node):
        return node in self.succ

    def __iter__(self):
        return iter(self.succ)

    def __len__(self):
        return len(self.succ)

    def __eq__(self,node):
        """
        Compare deux nœuds pour déterminer s'ils sont égaux.

        :param other: Autre nœud à comparer.
        :return: True si les nœuds ont le même nom et les mêmes fils.
        """
        if self.id==node.id:
            return True
        return False

    def number(self):
        """
        Retourne l'identifiant unique du nœud.

        :return: Identifiant unique du nœud.
        """
        return self.id

    def getname(self):
        """
        Retourne le nom du nœud.

        :return: Nom du nœud.
        """
        return self.name
        
    def ajouter_fils(self,names):
        """
        Crée un nouveau nœud avec un nom donné et l'ajoute comme fils.

        :param name: Nom du nœud fils à créer.
        """
        for elem in names:
            fils = Node(elem,father = self)
            if len(self.succ)==0:
                self.succ.append(fils)
            else:
                self.succ[-1].brother = fils
                self.succ.append(fils)
    
    def is_last(self):
        if self.brother is None:
            return True
        return False

    def is_non_terminal(self):
        return self.name in ["file","def_etoile","stmt_etoile","def","arg","next_arg","suite","simple_stmt","simple_stmt_tail","simple_stmt_tail_tail","argument","next_argument","stmt","else","expr_init","expr_logic","expr_logic_tail","expr_comp","expr_comp_tail","comp_op","expr_low","expr_low_tail","expr_high","expr_high_tail","expr_unary","expr_primary","expr_primary_extra","expr_primary_tail2","expr_primary_tail","const","root" ]
    
    def ajouter_fils_arbre(self,regle,terminé=False):
        if terminé:
            return self.getroot()
        production = regle.split(" -> ")
        production2 = production[1].split()
        noms = [elem for elem in production2 if not elem in ["NEWLINE","EOF",",","BEGIN","END"]]
        if self.is_non_terminal() :
            self.ajouter_fils(noms)
            return self.succ[0]
        else:
            if self.is_last() :
                    return self.father.ajouter_fils_arbre(regle)
            else:
                return self.brother.ajouter_fils_arbre(regle)
            
    def getroot(self):
        if self.father is None:
            return self
        return self.father.getroot()
    
    def next(self):
        if self.is_last():
            return self.father.next()
        else:
            return self.brother
        
    def to_mermaid(self):
        size = unique_id
        labels = []
        mermaid = "flowchart TD\n"
        file = deque([self])
        while(len(file)>0):
            node = file.popleft()
            for elem in node:
                file.append(elem)
                mermaid = mermaid + f"{node.id}[{node.name}] --> {elem.id}['{elem.name}']\n"
        return mermaid
    
    def dessine(self,name = "arbre syntaxique"):
        """
        Dessine l'arbre syntaxique en utilisant mermaid.

        Cette méthode crée une page html contenant l'arbre syntaxique.
        """

        root = self.getroot()
        mermaid = root.to_mermaid()
        html = """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Arbre syntaxique</title>
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <script>
                mermaid.initialize({
                    startOnLoad: true
                });
            </script>
        </head>
        <body>
            <h1>Arbre syntaxique</h1>
            <div class="mermaid">""" +f"""
                {mermaid}
            </div>
        </body>
        </html>
        """

        fichier = open(f"./{name}.html",'w+')
        fichier.write(html)
        fichier.close()

        webbrowser.open(f"./{name}.html")
       
# Exemple d'utilisation de la classe Node
if __name__ == "__main__":
    root = Node("Root")
    child1 = Node("Child1")
    child2 = Node("Child2")

    root.ajouter_fils_noeud(child1)
    root.ajouter_fils_noeud(child2)

    root.dessine()


