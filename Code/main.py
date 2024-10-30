from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken

Lex1 = Lexeur(lire_fichier("mini_python/variable.py"))

#print(lire_fichier("mini_python/variable.py"))

Tokens = Lex1.Tokenisation()
affichage_fichier("mini_python/variable.py")
print("\n")

for token in Tokens:
    print(repr(token))
    