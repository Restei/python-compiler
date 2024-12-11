import plotly.graph_objects as go
from igraph import Graph, EdgeSeq

# Identifiant unique global pour les nœuds
unique_id = 0

class Node:
    """
    Classe représentant un nœud dans l'arbre syntaxique.
    """

    def __init__(self, name):
        """
        Initialise un nœud avec un nom et un identifiant unique.

        :param name: Nom du nœud (représentant la règle ou le contenu syntaxique).
        """
        global unique_id
        self.id = unique_id  # Identifiant unique pour le nœud
        self.name = name  # Nom du nœud
        self.succ = []  # Liste des fils du nœud
        unique_id += 1

    def __repr__(self):
        return self.name

    def __getitem__(self, i):
        return self.succ[i]

    def __contains__(self, node):
        return node in self.succ

    def __iter__(self):
        return iter(self.succ)

    def __len__(self):
        return len(self.succ)

    def __eq__(self, other):
        """
        Compare deux nœuds pour déterminer s'ils sont égaux.

        :param other: Autre nœud à comparer.
        :return: True si les nœuds ont le même nom et les mêmes fils.
        """
        if self.name != other.name:
            return False
        if self.succ != other.succ:
            return False
        return True

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

    def ajouter_fils_noeud(self, node):
        """
        Ajoute un fils à ce nœud.

        :param node: Nœud fils à ajouter.
        """
        self.succ.append(node)

    def ajouter_fils(self, name):
        """
        Crée un nouveau nœud avec un nom donné et l'ajoute comme fils.

        :param name: Nom du nœud fils à créer.
        """
        self.succ.append(Node(name))

    def dessine(self):
        """
        Dessine l'arbre syntaxique en utilisant `plotly` et `igraph`.

        Cette méthode crée un graphique interactif représentant l'arbre syntaxique.
        """
        from collections import deque

        g = Graph()
        size = unique_id
        g.add_vertices(size)  # Ajoute des sommets au graphe
        labels = []  # Labels des nœuds pour affichage
        file = deque([self])  # File pour un parcours en largeur

        while file:
            node = file.popleft()
            labels.append(node.getname())
            for elem in node:
                g.add_edge(node.number(), elem.number())  # Ajoute des arêtes entre nœuds
                file.append(elem)

        # Calcul des positions des nœuds
        layout = g.layout("rt", root=[0])
        position = {k: layout[k] for k in range(size)}
        Y = [layout[k][1] for k in range(size)]
        M = max(Y)

        # Construction des listes d'arêtes pour l'affichage
        es = EdgeSeq(g)
        E = [e.tuple for e in g.es]

        L = len(position)
        Xn = [position[k][0] for k in range(L)]
        Yn = [2 * M - position[k][1] for k in range(L)]
        Xe = []
        Ye = []
        for edge in E:
            Xe += [position[edge[0]][0], position[edge[1]][0], None]
            Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

        # Création de la figure avec plotly
        fig = go.Figure()

        axis = dict(
            showline=False,  # Cache les lignes de l'axe
            zeroline=False,  # Cache la ligne zéro
            showgrid=False,  # Cache la grille
            showticklabels=False,  # Cache les labels
        )

        # Ajout des nœuds au graphique
        fig.add_trace(go.Scatter(
            x=Xn,
            y=Yn,
            mode='markers',
            name='noeuds',
            marker=dict(
                symbol='circle-dot',
                size=25,
                color='#6175c1',  # Couleur des nœuds
                line=dict(color='rgb(50,50,50)', width=1)
            ),
            text=labels,  # Affiche les noms des nœuds
            hoverinfo='text',
            opacity=1.0
        ))

        # Ajout des arêtes au graphique
        fig.add_trace(go.Scatter(
            x=Xe,
            y=Ye,
            mode='lines',
            line=dict(color='rgb(210,210,210)', width=2),
            hoverinfo='none',
        ))

        # Mise en forme finale
        fig.update_layout(
            font_size=12,
            showlegend=False,
            xaxis=axis,
            yaxis=axis,
            hovermode='closest',
        )

        # Affichage de l'arbre
        fig.show()


#R = Node("Root")
#R.ajouter_fils("R")
#
#R.ajouter_fils("RU")
#
#R.ajouter_fils("RUS")
#R[0].ajouter_fils("2")
#
#R[0].ajouter_fils("R5")
#R.dessine()