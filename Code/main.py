from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.table_des_symboles import *
from analyse_syntaxique.fonction_syntaxique import *


path = "mini_python/"

file = path + "test1.py"

Lex1 = Lexeur(lire_fichier(file))


Tokens,errors = Lex1.Tokenisation()


parse_with_tokens(tableau_des_symboles_directeur_ll1_ultime,Tokens,"file")

