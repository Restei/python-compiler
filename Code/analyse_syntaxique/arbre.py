
from collections import deque 
import re
import webbrowser
unique_id = 0
n=0
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
        self.mermaid_id = 0
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
    
    def __setitem__(self,i):
        self.succ[i]=i

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
        return self.name in ["file","def_etoile","stmt_etoile","def","arg","next_arg","suite","simple_stmt","simple_stmt_tail","expr_primary_tail2","expr_primary_tail","simple_stmt_tail_tail","argument","next_argument","stmt","expr_init","expr_logic","expr_logic_tail","expr_comp","expr_comp_tail","comp_op","expr_low","expr_low_tail","expr_high","expr_high_tail","expr_unary","expr_primary","expr_primary_extra","expr_primary_tail2","expr_primary_tail","const","root","Liste","element liste","Appel fonction","Else" ]
    
    def ajouter_fils_arbre(self,regle,term=None):
        production = regle.split(" -> ")
        production2 = production[1].split()
        if not term is None:
            for i in range(len(production2)):
                if production2[i] in ["ident","integer"]:
                    production2[i] = term
        noms = [elem for elem in production2 if not elem in ["NEWLINE","EOF",",","BEGIN","END",":"]]
            #Correction pour "for" et "range"
        if "for" in noms:
            index = noms.index("for")
            noms[index] = "Boucle for"

        if "range" in noms:
            index = noms.index("range")
            noms[index] = "Appel range"

        if self.name==production[0] :
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
    
    def suppr_vide(self):
        for elem in self:
            elem.suppr_vide()
        index = []
        i=0
        while i in range (len(self)):
            if self[i].is_non_terminal() and self[i].succ == []:
                self.succ = self.succ[:i] + self.succ[i+1:]
            else:
                i+=1
        


    def replace_identifier(self,liste):
        pile = [self]
        while len(pile)>0 and len(liste)>0:
            top = pile[0]
            pile = top.succ+pile[1:]
            if top.name=='ident':
                top.name = liste[0]
                liste = liste[1:]

    def leaf_to_node(self):
        succ = []
        count = 0
        term = ["def","return","print","if","for","and","or","+","-","*","//","<","<=",">",">=","==","=","!=","%","not","else"]
        for elem in self:
            if elem.name in term:
                count+=1
        if count==1:
            for i in range(len(self)):
                if self[i].name in term:
                    self.name = self[i].name
                else:
                    succ.append(self[i])
            self.succ = succ 
        for elem in self:
            elem.leaf_to_node()


    def binary_replace(self):


        # Liste des opérateurs binaires (y compris "-")
        binary_operators = {"and", "or", "+", "-", "*", "//", "<", "<=", ">", ">=", "==", "=", "!=", "%", "not"}

        # Vérifier si le nœud actuel est un non-terminal
        if self.is_non_terminal() and self.name not in ["expr_primary_extra","simple_stmt_tail_tail","expr_primary_tail"]:
            replaced = False  # Indicateur de remplacement

            for i in range(len(self)):
                child = self[i]
                # 🔹 Cas 1 : Un opérateur binaire doit être le nœud principal
                if child.name in binary_operators and self.name not in binary_operators:
                    # On échange le nom pour placer l'opérateur en tant que nœud principal
                    self.name, self[i].name = self[i].name, self.name
                    replaced = True
                    break  # Un seul remplacement par passage
            # 🔹 Cas 2 : Remplacement avec un terminal si aucun échange n'a eu lieu
            if not replaced:
                exceptions = {"root", "arg", "argument", "next_argument", "expr_primary", "suite"}
                if self.name not in exceptions:
                    for i, child in enumerate(self):
                        if not child.is_non_terminal():
                            # On échange avec un fils terminal si nécessaire
                            self.name, self[i].name = self[i].name, self.name
                            break  # Un seul échange suffit

        # Appliquer récursivement la transformation sur les enfants
        for child in self:
            child.binary_replace()

    def replace(self):

        for elem in self:
            elem.replace()
        if len(self)>1:
            succ = []
            for elem in self:
                if elem.name !="ε":
                    succ.append(elem)

            self.succ = succ
        if len(self) == 1 :
            if self.name != "suite" or self.succ[0].name == "ε":
                self.name = self[0].name
                self.succ = self[0].succ

    def clean(self):
        if len(self)>=1 :
                if self.name=="root" and self[0].name == "def_etoile":
                    Node_def = Node("Liste de Fonctions",self)
                    Node_def.succ = [self[0]]
                    self.succ = [Node_def] + self.succ[1:]
                i=0
                
                while i<len(self):
                    if self[i].name in ["def_etoile","stmt_etoile"]:
                        self.succ =self.succ[:i] + self.succ[i].succ + self.succ[i+1:]
                    elif self[i].name in ["(",")"] and self.name!="expr_primary_tail":
                        self.succ =self.succ[:i] + self.succ[i+1:]
                    else:
                        i+=1
                if self.name=="def" and self[0].name !="def":
                    self.name = self[0].name
                    self.succ = self.succ[1:]
                if self.name in ["arg","argument"]:
                    i=0
                    while i<len(self):
                        if self[i].name in ["next_arg","next_argument"]:
                            self.succ =self.succ[:i] + self.succ[i].succ + self.succ[i+1:]
                        i+=1
                if self.name in ["expr_primary_extra","simple_stmt_tail_tail"]:
                    i=0
                    while (i<len(self)):
                        if self[i].name in ["expr_primary_tail2","simple_stmt_tail_tail"]:
                            self.succ = self.succ[:i] + self.succ[i].succ + self.succ[i+1:]
                        else:
                            i+=1
                if self.name=="simple_stmt":
                    if self[1].name=="=" and len(self[1])==2:
                        node = self[0]
                        self.succ = self.succ[1:]
                        new_node = self.succ[0][0]
                        new_node.succ = [node] + new_node.succ
                        self[0].succ = self[0].succ[1:]
                        self.succ = [new_node] + self.succ
        for elem in self:
            elem.clean()

    def postclean(self):
        if len(self)>=1 :
            if self.name == "simple_stmt_tail":
                print(self[0].name, self[0].succ)
                self.name = self[0].name
                self.succ = self[0].succ
        if self.name == "expr_comp":
            print(self[0].name, self[0].succ)
            self.name = self[0].name
            self.succ = self[0].succ
        if self.name == "expr_primary":
            print(self[0].name, self[0].succ)
            self.name = self[0].name
            self.succ = self[0].succ
        
        for elem in self:
            elem.postclean()



    def rename(self):
    
    #Fonction qui renomme certains nœuds de l'AST pour le rendre plus abstrait et compréhensible.Elle fusionne également certains nœuds inutiles pour simplifier la structure.
    

        i = 0  # Index pour parcourir les enfants du nœud actuel

        while i < len(self):  # Parcourir les enfants du nœud
            # Cas 1 : Fusionner certains nœuds intermédiaires dans l'arbre
            if self[i].name in ["expr_logic", "simple_stmt", "expr_low", "expr_high", "expr_primary_tail"]:
                # Remplacer le nœud actuel par ses enfants pour éviter les structures inutiles
                self.succ = self.succ[:i] + self[i].succ + self.succ[i+1:]

            # Cas 2 : Gestion des listes et des appels de fonction
            elif self.name == "expr_primary":
                if self[i].name in ["[", "argument"]:
                    # Fusionner les nœuds "[]" et "argument" directement dans expr_primary
                    self.succ = self.succ[:i] + self[i].succ + self.succ[i+1:]
                elif self[i].name == "]":
                    # Transformer une structure de liste en un nœud unique "Liste"
                    self.name = "Liste"
                    self.succ = self.succ[:i]  # Supprimer les nœuds inutiles
                else:
                    i += 1

            # Cas 3 : Gestion des éléments d'une liste dans une expression
            elif self[i].name == "simple_stmt_tail_tail":
                self[i].name = "element liste"  # Renommer pour donner un sens abstrait
                i += 1

            elif self[i].name == "expr_primary_extra":
                # Si l'expression se termine par "]", c'est une liste, sinon c'est un appel de fonction
                if self[i][-1].name == "]":
                    self[i].name = "element liste"
                else:
                    self[i].name = "Appel fonction"
                i += 1

            # Cas 4 : Correction spécifique pour les boucles "for"
            elif self[i].name == "for":
                # Renommer explicitement le nœud pour qu'il soit abstrait et compréhensible
                self[i].name = "Boucle for"
                i += 1

            # Cas 5 : Correction spécifique pour "range"
            elif self[i].name == "range":
                # Transformer "range" en un nœud d'Appel de fonction "range"
                self[i].name = "Appel range"
                i += 1

            else:
                i += 1  # Passer au nœud suivant si aucune modification n'est faite

        # Cas 6 : Appliquer récursivement la transformation aux enfants restants
        for elem in self:
            elem.rename()
    

    def AST(self,name="AST"):
        self.name = "root"
        self.replace()
        self.leaf_to_node()
        self.clean()
        self.postclean()
        self.binary_replace()
        self.suppr_vide()
        self.rename()
        self.dessine(name)

    def depth(self):
        if self.succ == []:
            return 1
        else :
            return 1+max([elem.depth() for elem in self])
        
        
    
        
    def to_mermaid(self):
        """
        Génère une représentation Mermaid améliorée de l'arbre syntaxique.
        """
        mermaid = "flowchart TD\n"
        file = deque([self])
        count = 1
        while file:
            node = file.popleft()
            # Définir le style pour les nœuds terminaux et non terminaux
            node_style = ":::non_terminal" if node.is_non_terminal() else ":::terminal"
            for elem in node:
                elem.mermaid_id = count if elem.mermaid_id==0 else elem.mermaid_id
                count+=1
                file.append(elem)
                elem_style = ":::error" if elem.name == "erreur" else ""
                if node.name[0] in '+-*/%>':
                    mermaid += f'{node.mermaid_id}["\\{node.name}"]{node_style} --> {elem.mermaid_id}["{elem.name}"]{elem_style}\n'
                else:
                    mermaid += f'{node.mermaid_id}["{node.name}"]{node_style} --> {elem.mermaid_id}["{elem.name}"]{elem_style}\n'
        # Ajouter des définitions de style
        mermaid += """
        
        classDef non_terminal fill:#bbf3ff,stroke:#333,stroke-width:2px,shape:ellipse;
        classDef error fill:#fc1111,stroke:#333,stroke-width:2px,shape:ellipse;

        """
        return mermaid

        
    def dessine(self,name = "arbre syntaxique"):
        """
        Dessine l'arbre syntaxique en utilisant mermaid.

        Cette méthode crée une page html contenant l'arbre syntaxique.
        """

        root = self.getroot()
        mermaid = root.to_mermaid()
#        print(mermaid)
        html = """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">"""+f"<title>{name}</title>"+"""
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <script>
                mermaid.initialize({
                    startOnLoad: true
                });
            </script>
        </head>
        <body>""" + f"""
            <h1>{name}</h1>
            <div class="mermaid">
                {mermaid}
            </div>
        </body>
        </html>
        """
        #print(mermaid)

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


