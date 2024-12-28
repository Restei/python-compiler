import re
from analyse_lexicale.token import *

# Lit le contenu d'un fichier et le retourne
def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu

# Affiche le contenu d'un fichier avec une mise en évidence des caractères spéciaux comme '\n' et '\t'
def affichage_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
        print("La taille du contenu est:", len(contenu))
        for lettre in contenu:
            if lettre == "\n":
                print("\\n")  # Saut de ligne
            elif lettre == "\t":
                print("\\t")  # Tabulation
            else:
                print(lettre, end="")  
                
    return "Affichage terminé"

# Classe principale pour analyser lexicalement un contenu donné
class Lexeur:
    def __init__(self, contenu):
        self.contenu = contenu + " "  # Ajoute un espace à la fin pour éviter les erreurs d'analyse
        self.taille = len(self.contenu)
        self.position = -1  # Position actuelle dans le contenu
        self.ligne_position = 1  # Ligne actuelle
        self.curseur_position = 0  # Position globale dans le fichier
        self.charactere_actuelle = None  # Caractère courant
        self.token = None  # Token en cours de formation
        self.token_nombre = False  # Indique si le token courant est un nombre
        self.fin_fichier = False  # Indique si la fin du fichier est atteinte
        self.string = False  # Indique si le token est une chaîne de caractères
        self.is_indent = False  # Indique un début potentiel d'indentation
        self.variable_error = False  # Erreur liée à une variable invalide
        self.number_error = False  # Erreur liée à un nombre invalide
        self.count = 0  # Compteur pour l'indentation
        self.pile_indent = [0]  # Pile pour gérer les niveaux d'indentation
        self.errors = []  # Liste des erreurs lexicales détectées

    # Lit le prochain caractère et met à jour les attributs correspondants
    def lire(self):
        if self.curseur_position >= self.taille:
            self.fin_fichier = True
        else:
            self.position += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1

    # Revient au caractère précédent
    def retour(self):
        if self.curseur_position >= 1:
            if self.charactere_actuelle == '\n':
                self.ligne_position -= 1
            self.position -= 1
            self.curseur_position -= 1
            self.charactere_actuelle = self.contenu[self.position]

    # Prévisualise le prochain caractère sans l'avancer
    def peek(self):
        if self.curseur_position + 1 < len(self.contenu):
            return self.contenu[self.curseur_position + 1]
        return None

    # Passe à la prochaine ligne
    def next_line(self):
        while self.charactere_actuelle != '\n':
            self.lire()

    # Vérifie si le caractère actuel est un chiffre
    def chiffre(self):
        return self.charactere_actuelle.isdigit()

    # Vérifie si le caractère actuel est alphabétique ou un underscore
    def charactere(self):
        return self.charactere_actuelle.isalpha() or self.charactere_actuelle == '_'

    # Vérifie si le caractère est inconnu (non autorisé)
    def caractere_inconnu(self):
        caracteres_autorises = "!\"#%&'()*+,-./:<=>?[\\]^_`{|} "
        if self.charactere_actuelle.isalnum() or self.charactere_actuelle in caracteres_autorises:
            return False 
        return True 

    # Détermine si un caractère marque la fin d'un mot
    def fin_de_mot(self):
        fin = [',', '\n', ' ', '+', '-', ':', '(', ')', '[', ']', '/', '*', '=', '.','<','>']
        return self.charactere_actuelle in fin

    # Gère les opérateurs unaires
    def unary_operator(self):
        operator_type = TokenType.is_unary_operator(self.charactere_actuelle)
        if operator_type:
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.position)
        return None  

    # Gère les opérateurs binaires et unaires
    def binary(self):
        if self.curseur_position + 1 < self.taille:
            next_charactere = self.contenu[self.curseur_position]
            binary_token = self.charactere_actuelle + next_charactere

            operator_type = TokenType.is_binary_operator(binary_token)
            if operator_type:
                self.lire()  
                return OperatorBinaryToken(binary_token, self.ligne_position, self.position)
            else:
                return self.unary_operator()
        else:
            return self.unary_operator()

    # Analyse les mots-clés, identifiants, chaînes et nombres
    def mot_cle(self):
        keywords = {
            'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
            'def': 'DEF', 'return': 'RETURN', 'import': 'IMPORT', 'from': 'FROM', 
            'and':'AND', 'True':'TRUE','False':'FALSE','in':'IN','not':'NOT','or':'OR',
            'print':'PRINT','None':'NONE'
        }
        if self.variable_error or self.number_error:
            return UnknownToken(self.token, self.ligne_position, self.position)
        
        if self.token in keywords:
            return KeywordToken(self.token, self.ligne_position, self.position)
        
        elif self.token_nombre:
            if self.token[0]=='0':
                if len(self.token)>1:
                    self.errors.append(ZeroException(self.ligne_position, self.token))
                    return UnknownToken(self.token, self.ligne_position, self.position)
            return LiteralToken(self.token, self.ligne_position, self.position)
        
        elif self.string:
            return StringToken(self.token, self.ligne_position, self.position)
        
        else:
            return IdentifierToken(self.token, self.ligne_position, self.position)
