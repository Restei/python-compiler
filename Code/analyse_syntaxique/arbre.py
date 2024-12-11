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

    