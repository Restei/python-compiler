import re, sys
from analyse_lexicale.token import TokenType, BaseToken, KeywordToken, OperatorToken, LiteralToken, IdentifierToken, PunctuationToken, NewlineToken, OperatorUnaryToken, OperatorBinaryToken


def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu

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

class LexicalError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"Erreur lexicale à la ligne {line}, colonne {column}: {message}")    

class Lexeur:
    def __init__(self, contenu):
        self.contenu = contenu + " "
        self.taille = len(self.contenu)
        self.position = -1
        self.ligne_position = 1
        self.curseur_position = 0
        self.charactere_actuelle = None
        self.token = None
        self.token_nombre = False
        self.fin_fichier = False

    def lire(self):
        if self.curseur_position >= self.taille:
            self.fin_fichier = True
        else:
            self.position += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1

    def chiffre(self):
        return self.charactere_actuelle.isdigit()

    def charactere(self):
        return self.charactere_actuelle.isalpha() or self.charactere_actuelle == '_'

    def fin_de_mot(self):
        fin = [',', '\n', ' ', '+', '-', ':', '(', ')', '[', ']', '/', '*', '=', '.']
        return self.charactere_actuelle in fin

    def unary_operator(self):
        operator_type = TokenType.is_unary_operator(self.charactere_actuelle)
        if operator_type:
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.position)
        return None  

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

    def mot_cle(self):
        keywords = {
            'if': 'IF', 'elif': 'ELIF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
            'def': 'DEF', 'return': 'RETURN', 'import': 'IMPORT', 'from': 'FROM'
        }

        if self.token in keywords:
            return KeywordToken(self.token, self.ligne_position, self.position)
        elif self.token_nombre:
            return LiteralToken(self.token, self.ligne_position, self.position)
        else:
            return IdentifierToken(self.token, self.ligne_position, self.position)

    def Identification(self, tokens):
        if (self.charactere() or self.charactere_actuelle == '_') and (self.token is None):
            self.token = self.charactere_actuelle

        elif self.token:
            if not self.fin_de_mot():
                self.token += self.charactere_actuelle
                # Vérification de la longueur du mot
                
            else:
                if len(self.token) > 50:
                    raise LexicalError("Le mot est trop long (plus de 50 caractères)", self.ligne_position, self.position)
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False

        elif self.chiffre() and (not self.token):
            self.token = self.charactere_actuelle
            self.token_nombre = True
            if self.charactere_actuelle == '0':
                tokens.append(LiteralToken(self.token, self.ligne_position, self.position))
                self.token = None
                self.token_nombre = False
            else:
                self.token = self.charactere_actuelle
                self.token_nombre = True    # Continue collecting digits for the number

        # Vérifie si le token actuel est un nombre entier et s'il est terminé par un séparateur
        elif self.token_nombre:
            if self.charactere_actuelle.isdigit():
                self.token += self.charactere_actuelle
            else:
                # Si le token contient des caractères non numériques et que ce n'est pas un nombre valide
                if not self.token.isdigit():
                    raise LexicalError(f"Nombre invalide: '{self.token}'", self.ligne_position, self.position)
                tokens.append(LiteralToken(self.token, self.ligne_position, self.position))
                self.token = None
                self.token_nombre = False    

                # Vérification de la valeur numérique de l'entier
                try:
                    number = int(self.token)
                    # Limite des entiers
                    if abs(number) > sys.maxsize:
                        raise LexicalError("La valeur de l'entier dépasse la limite autorisée", self.ligne_position, self.position)
                except ValueError:
                    raise LexicalError(f"Nombre entier non valide: '{self.token}'", self.ligne_position, self.position)

            tokens.append(LiteralToken(self.token, self.ligne_position, self.position))
            self.token = None
            self.token_nombre = False

        elif self.charactere_actuelle == '\n':
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False
            tokens.append(NewlineToken(self.ligne_position, self.position))

        elif self.charactere_actuelle in '(){}[]':
            tokens.append(PunctuationToken(self.charactere_actuelle, self.ligne_position, self.position))

        else:
            if self.token:
                tokens.append(self.mot_cle())
                self.token = None
                self.token_nombre = False

            operator_token = self.binary()  
            if operator_token:
                tokens.append(operator_token)

    def Tokenisation(self):
        tokens = []

        while not self.fin_fichier:
            try:
                self.lire()
                self.Identification(tokens)
            except LexicalError as e:
                print(f"Erreur lexicale détectée à la ligne {self.ligne_position}, colonne {self.position}: {e}")
                self.token = None  # Réinitialise le token et continue après l'erreur

        # Ajouter le token EOF à la fin
        tokens.append(BaseToken(TokenType.EOF, '', self.ligne_position, self.position))
        return tokens
