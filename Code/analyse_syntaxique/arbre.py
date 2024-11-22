import plotly.graph_objects as go
from igraph import *
import igraph as ig
class Node:
    def __init__(self,name):
        self.name = name
        self.succ = []
        
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
        if self.name != node.name:
            return False
        else:
            if self.succ != node.succ:
                return False
            return True

    def taille(self):
        size = 1
        for elem in self.succ:
            if elem.succ != []:
                size += elem.taille()
            else:
                size+= 1
        return size

    def ajouter_fils(self,node):
        self.succ.append(Node(node)) 

    def dessine(self):
        size = self.taille()
        g= Graph()
        g.add_vertices(size)
        

        def parcours_largeur(node):
            from collections import deque
            
            num_succ = len(node)
            origin = 0
            current = 1
            file = deque([node])
            X = [node]
            marque = [node]

            while(len(file)>0):
                current_node= file.popleft()
                for i in range (len(X)):
                    if X[i]==current_node:
                        origin = i

                for elem in current_node:
                    if elem not in marque :
                        file.append(elem)
                        marque.append(elem)
                        g.add_edge(origin,current)
                        current+=1            

        parcours_largeur(self)

        layout = g.layout("rt",root = [0])
        
        
        position = {k: layout[k] for k in range(size)}
        Y = [layout[k][1] for k in range(size)]
        M = max(Y)

        es = EdgeSeq(g) # sequence of edges
        E = [e.tuple for e in g.es] # list of edges

        L = len(position)
        Xn = [position[k][0] for k in range(L)]
        Yn = [2*M-position[k][1] for k in range(L)]
        Xe = []
        Ye = []
        for edge in E:
            Xe+=[position[edge[0]][0],position[edge[1]][0], None]
            Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

        labels = [0,1,2]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
        fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='bla',
                  marker=dict(symbol='circle-dot',
                                size=18,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  ))
        fig.show()

        
        

R = Node("Root")
R.ajouter_fils("R")

R.ajouter_fils("RU")

R.ajouter_fils("RUS")
R[0].ajouter_fils("2")

R[0].ajouter_fils("R5")

R.dessine()