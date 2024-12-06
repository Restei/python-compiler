<<<<<<< HEAD
from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.table_des_symboles import *
from analyse_syntaxique.fonction_syntaxique_dictionnaire import *

path = "mini_python/"
fichier = "test1.py"
=======
from analyse_syntaxique.fonction_syntaxique import * 
from analyse_syntaxique.GrammairesLL1 import *

# Charger le contenu du fichier source
fichier_source = lire_fichier("Code/mini_python/expression.py")
>>>>>>> df908c0456185923192398672dadc3fca0fcb5f4

# Étape 1 : Analyse lexicale
Lex1 = Lexeur(fichier_source)  # Instancie le lexeur
Lex1.Tokenisation()  # Génère les tokens et détecte les erreurs lexicales

if Lex1.errors:
    # Si des erreurs lexicales sont détectées, les afficher
    print("Erreurs lexicales détectées :")
    for erreur in Lex1.errors:
        print(erreur)
else:
    print("Analyse lexicale réussie. Les tokens sont prêts pour l'analyse syntaxique.")

# Étape 2 : Analyse syntaxique
try:
    parser = LL1Parser(fichier_source)  # Instancie le parseur LL(1)
    parser.parse()  # Lance l'analyse syntaxique

    if parser.errors:
        # Si des erreurs syntaxiques sont détectées, les afficher
        print("\nErreurs syntaxiques détectées :")
        for erreur in parser.errors:
            print(erreur)
    else:
        print("\nAnalyse syntaxique réussie. Aucun problème détecté.")
except Exception as e:
    print(f"Une erreur critique est survenue : {e}")

<<<<<<< HEAD
for token in Tokens:
    print(repr(token))
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

parse_with_tokens(ll1_table,Tokens,"file")
=======
>>>>>>> df908c0456185923192398672dadc3fca0fcb5f4
