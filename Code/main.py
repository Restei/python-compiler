from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier

Lex1 = Lexeur(lire_fichier("mini_python/expression.py"))

#print(lire_fichier("mini_python/variable.py"))
while(Lex1.fin_fichier != True):
    Lex1.lire()
    Lex1.Tokenisation()
    