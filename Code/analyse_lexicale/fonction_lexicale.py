import re
from token import TokenType, BaseToken, KeywordToken, OperatorToken, LiteralToken, IdentifierToken, PunctuationToken, NewlineToken, OperatorUnaryToken, OperatorBinaryToken


def lire_fichier(source):
    with open(source, 'r') as fichier:
        contenu = fichier.read()
    return contenu


class Lexeur:
    def __init__(self, contenu):
        self.contenu = contenu
        self.position = -1
        self.ligne_position = 1
        self.curseur_position = 0
        self.charactere_actuelle = None
        self.token = None
        self.token_nombre = False
        self.fin_fichier = False

    def lire(self):
        if self.curseur_position >= len(self.contenu):
            self.fin_fichier = True
        else:
            self.position += 1
            self.curseur_position += 1
            self.charactere_actuelle = self.contenu[self.position]
            if self.charactere_actuelle == '\n':
                self.ligne_position += 1

    def peek(self):
        if self.curseur_position + 1 < len(self.contenu):
            return self.contenu[self.curseur_position + 1]
        return None

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
            
            return OperatorUnaryToken(self.charactere_actuelle, self.ligne_position, self.curseur_position)
        return None  

    def binary(self):
      
        if self.curseur_position + 1 < len(self.contenu):
            next_charactere = self.contenu[self.curseur_position]
            binary_token = self.charactere_actuelle + next_charactere

            operator_type = TokenType.is_binary_operator(binary_token)
            if operator_type:
                
                self.lire()  
                return OperatorBinaryToken(binary_token, self.ligne_position, self.curseur_position)
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
            return KeywordToken(self.token, self.ligne_position, self.curseur_position)
        elif self.token_nombre:
            return LiteralToken(self.token, self.ligne_position, self.curseur_position)
        else:
            return IdentifierToken(self.token, self.ligne_position, self.curseur_position)

    def Tokenisation(self):
        tokens = []

        while not self.fin_fichier:
            self.lire()

            
            if self.charactere() or self.charactere_actuelle == '_':
                if self.token is None:
                    self.token = self.charactere_actuelle
                elif not self.fin_de_mot():
                    self.token += self.charactere_actuelle
                else:
                    
                    tokens.append(self.mot_cle())
                    self.token = None

            
            elif self.chiffre():
                if not self.token:
                    self.token = self.charactere_actuelle
                    self.token_nombre = True
                elif self.token_nombre:
                    self.token += self.charactere_actuelle
                else:
                    tokens.append(self.mot_cle())
                    self.token = self.charactere_actuelle
                    self.token_nombre = True

            
            elif self.charactere_actuelle == '\n':
                if self.token:
                    tokens.append(self.mot_cle())
                    self.token = None
                    self.token_nombre = False
                tokens.append(NewlineToken(self.ligne_position, self.curseur_position))

            
            elif self.charactere_actuelle in '(){}[]':
                tokens.append(PunctuationToken(self.charactere_actuelle, self.ligne_position, self.curseur_position))

            
            else:
                if self.token:
                    tokens.append(self.mot_cle())
                    self.token = None
                    self.token_nombre = False

                
                operator_token = self.binary()  
                if operator_token:
                    tokens.append(operator_token)

        # Ajouter le token EOF à la fin
        tokens.append(BaseToken(TokenType.EOF, '', self.ligne_position, self.curseur_position))
        return tokens


  
