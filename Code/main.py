from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.table_des_symboles import *

path = "mini_python/"

fichier = "error.py"


file = path + fichier

Lex1 = Lexeur(lire_fichier(file))

#print(lire_fichier("mini_python/variable.py"))

Tokens,errors = Lex1.Tokenisation()
#affichage_fichier(file)
print("\n")

for token in Tokens:
    print(repr(token))

#representation_TDS(creation_TDS(Tokens))
