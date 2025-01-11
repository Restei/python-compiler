import re
from analyse_lexicale.token import *

# Fonction pour lire le contenu d'un fichier
def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu

# Fonction pour afficher le contenu du fichier avec la gestion des caractères spéciaux
def affichage_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
        print("La taille du contenu est:", len(contenu))
        # Afficher chaque caractère, en particulier pour les sauts de ligne et tabulations
        for lettre in contenu:
            if lettre == "\n":
                print("\\n")  # Saut de ligne
            elif lettre == "\t":
                print("\\t")  # Tabulation
            else:
                print(lettre, end="")  
                
    return "Affichage terminé"

class Lexeur:
    # Initialisation du Lexeur avec les paramètres nécessaires
    def __init__(self, contenu):
        self.contenu = contenu + " "  # Ajout d'un espace à la fin pour gérer la fin du contenu
        self.taille = len(self.contenu)
        self.position = -1  # Position actuelle dans le contenu
        self.ligne_position = 1  # Position de la ligne
        self.curseur_position = 0  # Position du curseur
        self.charactere_actuelle = None  # Caractère actuel
        self.token = None  # Token en cours de traitement
        self.token_nombre = False  # Booléen pour gérer les nombres
        self.fin_fichier = False  # Booléen pour vérifier la fin du fichier
        self.string = False  # Booléen pour vérifier si on est dans une chaîne
        self.is_indent = False  # Booléen pour gérer les indentations
        self.variable_error = False  # Booléen pour les erreurs de variable
        self.number_error = False  # Booléen pour les erreurs de nombre
        self.count = 0  # Compteur pour l'indentation
        self.pile_indent = [0]  # Pile d'indentation
        self.errors = []  # Liste pour stocker les erreurs

    # Lire le caractère suivant dans le fichier
    def lire(self):
        if self.curseur_position >= self.taille:
            self.fin_fichier = True  # On marque la fin du fichier
        else:
            self.position += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1

    # Revenir en arrière d'un caractère
    def retour(self):
        if self.curseur_position >= 1:
            if self.charactere_actuelle == '\n':
                self.ligne_position -= 1
            self.position -= 1
            self.curseur_position -= 1
            self.charactere_actuelle = self.contenu[self.position]

    # Fonction peek pour regarder le prochain caractère sans le lire
    def peek(self):
        if self.curseur_position + 1 < len(self.contenu):
            return self.contenu[self.curseur_position + 1]
        return None

    # Avancer jusqu'à la fin de la ligne
    def next_line(self):
        while self.charactere_actuelle != '\n':
            self.lire()

    # Vérifier si le caractère actuel est un chiffre
    def chiffre(self):
        return self.charactere_actuelle.isdigit()

    # Vérifier si le caractère actuel est une lettre ou un underscore
    def charactere(self):
        return self.charactere_actuelle.isalpha() or self.charactere_actuelle == '_'

    # Vérifier si le caractère est un caractère inconnu
    def caractere_inconnu(self):
        caracteres_autorises = "!\"#%&'()*+,-./:<=>?[\\]^_`{|} "
        if self.charactere_actuelle.isalnum() or self.charactere_actuelle in caracteres_autorises:
            return False 
        return True 

    # Vérifier si on a atteint la fin d'un mot
    def fin_de_mot(self):
        fin = [',', '\n', ' ', '+', '-', ':', '(', ')', '[', ']', '/', '*', '=', '.','<','>']
        return self.charactere_actuelle in fin

    # Gérer les opérateurs unaires (ex : -x)
    def unary_operator(self):
        operator_type = TokenType.is_unary_operator(self.charactere_actuelle)
        if operator_type:
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.position)
        return None  

    # Gérer les opérateurs binaires (ex : +, -, *)
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

    # Vérification des mots-clés et identification des tokens
    def mot_cle(self):
        keywords = {
            'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
            'def': 'DEF', 'return': 'RETURN', 'import': 'IMPORT', 'from': 'FROM', 
            'and':'AND', 'True':'TRUE','False':'FALSE','in':'IN','not':'NOT','or':'OR',
            'print':'PRINT','None':'NONE'
        }
        # Si une erreur de variable ou de nombre est survenue, on renvoie un token inconnu
        if self.variable_error or self.number_error:
            return UnknownToken(self.token, self.ligne_position, self.position)
        
        # Vérifier si le token est un mot-clé
        if self.token in keywords:
            return KeywordToken(self.token, self.ligne_position, self.position)
        
        # Si c'est un nombre
        elif self.token_nombre:
            if self.token[0]=='0':  # Vérifier les nombres qui commencent par 0
                if len(self.token) > 1:
                    self.errors.append(ZeroException(self.ligne_position, self.token))
                    return UnknownToken(self.token, self.ligne_position, self.position)
            return LiteralToken(self.token, self.ligne_position, self.position)
        
        # Si c'est une chaîne de caractères
        elif self.string:
            return StringToken(self.token, self.ligne_position, self.position)
        
        # Sinon, c'est un identifiant
        else:
            return IdentifierToken(self.token, self.ligne_position, self.position)

    # Fonction pour identifier les éléments de l'entrée (indentation, commentaires, mots-clés, etc.)
    def Identification(self,tokens):
        if self.is_indent == True and self.charactere_actuelle != '\n':
            if self.charactere_actuelle == ' ' and not self.fin_fichier:
                self.count += 1  # Comptabiliser les espaces pour l'indentation
            else:
                if self.fin_fichier:
                    self.count -= 1
                self.retour()
                self.is_indent = False
                if self.count == self.pile_indent[0]:
                    pass
                elif self.count > self.pile_indent[0]:
                    self.pile_indent = [self.count] + self.pile_indent  # Ajouter une nouvelle indentation
                    tokens.append(IndentToken(self.ligne_position, self.position))
                    self.count = 0
                else:
                    if self.count in self.pile_indent:
                        while self.count != self.pile_indent[0]:
                            tokens.append(DedentToken(self.ligne_position, self.position))
                            self.pile_indent = self.pile_indent[1:]
                            self.pile_indent[0] = self.pile_indent[0]
                    else:
                        self.errors.append(IndentException(self.ligne_position))
        
        # Si un commentaire commence par #
        elif self.charactere_actuelle == '#':
            self.next_line()  # Ignorer le reste de la ligne
            self.retour()
        
        # Si le caractère est une lettre ou un underscore, commencer à identifier un mot
        elif (self.charactere() or self.charactere_actuelle == '_') and (self.token is None) and (not self.string):
            self.token = self.charactere_actuelle

        # Si le caractère est un guillemet, c'est le début d'une chaîne
        elif (self.charactere_actuelle == '"') and (self.token is None) and (not self.string):
            self.token = self.charactere_actuelle
            self.string = True

        # Si on est dans une chaîne et qu'on rencontre un guillemet, on termine la chaîne
        elif self.token and (self.string):
            if self.charactere_actuelle != '"':
                self.token += self.charactere_actuelle
            else:
                self.token += self.charactere_actuelle
                tokens.append(self.mot_cle())
                self.token = None
                self.string = False

        # Si on est dans un mot, continuer à l'identifier
        elif self.token and not self.string:
            if not self.fin_de_mot():
                if (not self.charactere()) and (not self.chiffre()) and (not self.token_nombre):
                    self.variable_error = True  # Erreur de variable si le caractère n'est ni une lettre ni un chiffre
                if self.token_nombre and not self.chiffre():
                    self.number_error = True  # Erreur de nombre si le caractère n'est pas un chiffre
                self.token += self.charactere_actuelle
                # Vérification de la longueur du nombre (par exemple, 50 caractères maximum)
                if self.token_nombre and len(self.token) > 50:
                    # Vérifier si l'erreur a déjà été ajoutée pour ce nombre
                    if not any(isinstance(e, NumberTooLongException) and e.token == self.token for e in self.errors):
                        self.errors.append(NumberTooLongException(self.ligne_position, self.token))
                    self.token = None  # Réinitialiser le token pour éviter d'ajouter un nombre trop long
                    self.token_nombre = False  # Réinitialiser le flag de nombre
                    return  # Sortir immédiatement pour ne pas ajouter un token trop long
            else:
                # Ajouter des erreurs si nécessaire
                if self.variable_error:
                    self.errors.append(UnknowCaractersInVariable(self.ligne_position, self.token))
                if self.number_error:
                    self.errors.append(AlphainNumberException(self.ligne_position, self.token))
                tokens.append(self.mot_cle())  # Ajouter le token à la liste
                self.token = None
                self.token_nombre = False
                self.variable_error = False
                self.number_error = False
                self.Identification(tokens)  # Continuer l'identification

        # Si le caractère est un chiffre, commencer à identifier un nombre
        elif self.chiffre() and (not self.token) and (not self.string):
            self.token = self.charactere_actuelle
            self.token_nombre = True

        # Si on rencontre un saut de ligne, ajouter un token de nouvelle ligne
        elif self.charactere_actuelle == '\n':
            tokens.append(NewlineToken(self.ligne_position, self.position))
            while self.peek() == '\n':  # Passer les éventuels sauts de ligne multiples
                self.lire()
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
            self.is_indent = True  # Nouvelle indentation possible
            self.count = 0

        # Gérer les ponctuations (parenthèses, crochets, virgules, etc.)
        elif self.charactere_actuelle in '(){}[]:,' and not self.string:
            tokens.append(PunctuationToken(self.charactere_actuelle, self.ligne_position, self.position))

        # Vérifier les opérateurs binaires ou inconnus
        else:
            operator_token = self.binary()  
            if operator_token:
                tokens.append(operator_token)
            elif self.caractere_inconnu():
                tokens.append(UnknownToken(self.charactere_actuelle, self.ligne_position, self.position))
                self.errors.append(UnknowCaracters(self.ligne_position, self.charactere_actuelle))

    # Fonction principale de tokenisation
    def Tokenisation(self):
        tokens = []
        while not self.fin_fichier:
            self.lire()
            self.Identification(tokens)
        
        # Ajouter le token EOF à la fin
        tokens.append(BaseToken(TokenType.EOF, '', self.ligne_position, self.position))
        tokens2 = [tokens[0]]  # Liste des tokens sans sauts de ligne inutiles
        for elem in tokens[1:]:
            if elem.type == TokenType.NEWLINE and (tokens2[-1].type == TokenType.NEWLINE or tokens2[-1].type == TokenType.BEGIN or tokens2[-1].type == TokenType.END):
                continue
            else:
                tokens2.append(elem)
        return tokens2, self.errors  # Retourner les tokens et les erreurs
