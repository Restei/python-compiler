# Test de variable avec des caractères inconnus
var@name = 10  # @ dans un identifiant 

# Test de nombre avec lettres
num123abc = 100  # Lettres dans un nombre 

# Test de nombre qui commence par zéro
zero_number = 0123  # Nombre commençant par 0 

# Test d'une indentation incorrecte
def func():
    print("Hello")
  print("World")   # Mauvaise indentation 

# Test de nombre trop long
long_number = 123456789012377777777777777777777777777777777777777777777777777777777777774567890  # Nombre trop long 

# Test de caractère inconnu
unknown_char = $&*#  # Caractères non autorisés dans une variable 

# Test de chaîne de caractères mal formée
bad_string = "This is a string without closing quote  # Devrait échouer, guillemet de fin manquant

