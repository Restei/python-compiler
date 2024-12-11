import plotly.graph_objects as go
from igraph import *
import igraph as ig



#########################################################################################################################################################
#                                                                                                                                                       #
#        
#        Création fils fera n (avec .split(' ') et mettra le nom des noeuds plus tard) noeud et les modifiera après                                                                                                                                               #
#        Modification fils 1 + Frères                                                                                                                                               #
#                                                                                                                                                        #
#                                                                                                                                                       #
#                                                                                                                                                       #
#                                                                                                                                                       #
#########################################################################################################################################################



















unique_id = 0

class Node:
    def __init__(self,name,father= None):
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
        if self.id==node.id:
            return True
        return False

    def number(self):
        return self.id

    def getname(self):
        return self.name
        
    def ajouter_fils(self,names):
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
        print(noms)
        if self.is_non_terminal() :
            self.ajouter_fils(noms)
            return self.succ[0]
        else:
            print(self)
            if self.is_last() :
                    print(self)
                    return self.father.ajouter_fils_arbre(regle)
            else:
                return self.brother.ajouter_fils_arbre(regle)
            
    def getroot(self):
        node = self
        while not node.father is None:
            node = self.father
        return node
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

Sortie = ["file -> NEWLINE stmt EOF ","stmt -> simple_stmt NEWLINE","simple_stmt -> ident simple_stmt_tail","simple_stmt_tail -> = expr_init","expr_init -> expr_primary","expr_primary -> const","const -> integer","stmt_etoile -> stmt stmt_etoile","stmt -> simple_stmt NEWLINE","simple_stmt -> ident simple_stmt_tail","simple_stmt_tail ->  = expr_init","expr_init -> expr_logic","expr_logic -> expr_comp ","expr_comp -> expr_low ","expr_low -> expr_high ","expr_high -> expr_unary ","expr_unary -> expr_primary","expr_primary -> const","const -> integer","stmt_etoile -> stmt stmt_etoile","stmt -> simple_stmt NEWLINE","simple_stmt -> ident simple_stmt_tail","simple_stmt_tail ->  = expr_init","expr_init -> expr_logic","expr_logic -> expr_comp expr_logic_tail","expr_comp -> expr_low expr_comp_tail","expr_low -> expr_high expr_low_tail","expr_high -> expr_unary","expr_unary -> expr_primary","expr_primary -> expr_primary_extra","expr_primary_extra -> ident","expr_low_tail -> + expr_high expr_low_tail","expr_high -> expr_unary expr_high_tail","expr_unary -> ident "]

Sortie2 = ['file -> NEWLINE def_etoile stmt stmt_etoile EOF', 'def_etoile -> vide', 'stmt -> simple_stmt NEWLINE', 'simple_stmt -> ident simple_stmt_tail', 'simple_stmt_tail -> simple_stmt_tail_tail = expr_init', 'simple_stmt_tail_tail -> vide', 'expr_init -> expr_logic', 'expr_logic -> expr_comp expr_logic_tail', 'expr_comp -> expr_low expr_comp_tail', 'expr_low -> expr_high expr_low_tail', 'expr_high -> expr_unary expr_high_tail', 'expr_unary -> expr_primary', 'expr_primary -> const', 'const -> integer', 'expr_high_tail -> vide', 'expr_low_tail -> vide', 'expr_comp_tail -> vide', 'expr_logic_tail -> vide', 'stmt_etoile -> stmt stmt_etoile', 'stmt -> simple_stmt NEWLINE', 'simple_stmt -> ident simple_stmt_tail', 'simple_stmt_tail -> simple_stmt_tail_tail = expr_init', 'simple_stmt_tail_tail -> vide', 'expr_init -> expr_logic', 'expr_logic -> expr_comp expr_logic_tail', 'expr_comp -> expr_low expr_comp_tail', 'expr_low -> expr_high expr_low_tail', 'expr_high -> expr_unary expr_high_tail', 'expr_unary -> expr_primary', 'expr_primary -> const', 'const -> integer', 'expr_high_tail -> vide', 'expr_low_tail -> vide', 'expr_comp_tail -> vide', 'expr_logic_tail -> vide', 'stmt_etoile -> stmt stmt_etoile', 'stmt -> simple_stmt NEWLINE', 'simple_stmt -> ident simple_stmt_tail', 'simple_stmt_tail -> simple_stmt_tail_tail = expr_init', 'simple_stmt_tail_tail -> vide', 'expr_init -> expr_logic', 'expr_logic -> expr_comp expr_logic_tail', 'expr_comp -> expr_low expr_comp_tail', 'expr_low -> expr_high expr_low_tail', 'expr_high -> expr_unary expr_high_tail', 'expr_unary -> expr_primary', 'expr_primary -> expr_primary_extra', 'expr_primary_extra -> ident expr_primary_tail', 'expr_primary_tail -> expr_primary_tail2', 'expr_primary_tail2 -> vide', 'expr_high_tail -> vide', 'expr_low_tail -> + expr_high expr_low_tail', 'expr_high -> expr_unary expr_high_tail', 'expr_unary -> expr_primary', 'expr_primary -> expr_primary_extra', 'expr_primary_extra -> ident expr_primary_tail']
        
if __name__=="__main__":
    root = Node("root")
    noeud = root
    for regle in Sortie:
        noeud = noeud.ajouter_fils_arbre(regle)

    #print(noeud.succ)
    root.dessine()

