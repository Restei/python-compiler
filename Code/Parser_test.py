from analyse_syntaxique.fonction_syntaxique import LL1Parser


# Ouvrir le fichier contenant le code à tester
with open("mini_python/expression.py", "r") as file:
    source_code = file.read()  # Lire tout le contenu du fichier



parser = LL1Parser(source_code) 
parser.parse() 


