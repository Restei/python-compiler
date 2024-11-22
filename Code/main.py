from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken

path = "mini_python/"
<<<<<<< HEAD
fichier = "complique.py"
=======
fichier = "erreurs.py"
>>>>>>> origin/main

file = path + fichier

Lex1 = Lexeur(lire_fichier(file))

#print(lire_fichier("mini_python/variable.py"))

Tokens,errors = Lex1.Tokenisation()
#affichage_fichier(file)
print("\n")

for token in Tokens:
    print(repr(token))
    
for error in errors:
<<<<<<< HEAD
    print(repr(error))    
=======
    print(repr(error))

    
>>>>>>> origin/main
