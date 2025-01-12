# Test de variable avec des caractères inconnus
var@name = 10  # @ dans un identifiant (devrait échouer)

# Test de nombre avec lettres
num123abc = 100  # Lettres dans un nombre (devrait échouer)

# Test de nombre qui commence par zéro
zero_number = 0123  # Nombre commençant par 0 (devrait échouer)

# Test d'une indentation incorrecte
def func():
    print("Hello")
  print("World")   # Mauvaise indentation (devrait échouer)

# Test de nombre trop long
long_number = 123456789012377777777777777777777777777777777777777777777777777777777777774567890  # Nombre trop long (devrait échouer)

# Test de caractère inconnu
unknown_char = $&*#  # Caractères non autorisés dans une variable (devrait échouer)

# Test de chaîne de caractères mal formée
bad_string = "This is a string without closing quote  # Devrait échouer, guillemet de fin manquant

