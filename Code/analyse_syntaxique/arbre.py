import plotly.graph_objects as go
from igraph import *
import igraph as ig


unique_id = 0

class Node:
    def __init__(self,name):
        global unique_id
        self.id = unique_id 
        self.name = name
        self.succ = []
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
        if self.name != node.name:
            return False
        else:
            if self.succ != node.succ:
                return False
            return True

    def number(self):
        return self.id

    def getname(self):
        return self.name
    
    def ajouter_fils_noeud(self,node):
        self.succ.append(node) 


    def ajouter_fils(self,node):
        self.succ.append(Node(node)) 



    def dessine(self):
        from collections import deque
        
        g= Graph()
        size = unique_id
        g.add_vertices(size)
        labels = []
        file = deque([self])
        while (len(file)>0):
            node = file.popleft()
            labels.append(node.getname())
            for elem in node:
                g.add_edge(node.number(),elem.number())
                file.append(elem)

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

        fig = go.Figure()

        axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

        fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='noeuds',
                  marker=dict(symbol='circle-dot',
                                size=25,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=1.0
                  ))
        
        fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=2),
                   hoverinfo='none',
                   ))
        fig.update_layout(
              font_size=12,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              hovermode='closest',
              )
        

        
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