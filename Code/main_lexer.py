from analyse_lexicale.fonction_lexicale import *
from analyse_lexicale.token import *

# Charger le contenu du fichier erreurs.py
contenu = lire_fichier("mini_python/erreurs_lex.py")

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
