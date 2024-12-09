from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.table_des_symboles import *
from analyse_syntaxique.fonction_syntaxique_dictionnaire import *


path = "mini_python/"
fichier = "test1.py"

file = path + fichier

Lex1 = Lexeur(lire_fichier(file))

#print(lire_fichier("mini_python/variable.py"))

Tokens,errors = Lex1.Tokenisation()
#affichage_fichier(file)
print("\n")

#for token in Tokens:
#    print(repr(token))
#    
#for error in errors:
#    print(repr(error))

#representation_TDS(creation_TDS(Tokens))

#try:
#    parser = LL1Parser("""
#                       a = 0""")  # Instancie le parseur LL(1)
#    parser.parse()  # Lance l'analyse syntaxique
#
#    if parser.errors:
#        # Si des erreurs syntaxiques sont détectées, les afficher
#        print("\nErreurs syntaxiques détectées :")
#        for erreur in parser.errors:
#            print(erreur)
#    else:
#        print("\nAnalyse syntaxique réussie. Aucun problème détecté.")
#except Exception as e:
#    print(f"Une erreur critique est survenue : {e}")

parse_with_tokens(tableau_des_symboles_directeur_ll1_ultime,Tokens,"file")
#parse_with_tokens_and_build_tree(grammar,Tokens,"file")
