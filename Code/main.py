from analyse_lexicale.fonction_lexicale import Lexeur,lire_fichier,affichage_fichier
from analyse_lexicale.token import TokenType, BaseToken
from analyse_syntaxique.table_des_symboles import *
from analyse_syntaxique.fonction_syntaxique import *


path = "mini_python/"

file = path + "expression.py"


contenu = lire_fichier(file)

# Créer un objet Lexeur
lexeur = Lexeur(contenu)

# Effectuer la tokenisation
tokens, erreurs = lexeur.Tokenisation()

# Affichage des tokens extraits
print("Tokens extraits :")
for token in tokens:
    print(token)

# Affichage des erreurs rencontrées
if erreurs:
    print("\nErreurs rencontrées :")
    for erreur in erreurs:
        print(erreur)
# Effectuer le parsing avec les tokens extraits
parse_with_tokens(tableau_des_symboles_directeur_ll1_ultime,tokens,"file")

