from enum import Enum


class TokenType(Enum):
    # Enumération des types de tokens supportés
    IDENTIFIER = 'IDENTIFIER'  
    NUMBER = 'NUMBER'  
    KEYWORD = 'KEYWORD'  
    OPERATOR_UNARY = 'OPERATOR_UNARY'  
    OPERATOR_BINARY = 'OPERATOR_BINARY'  
    PUNCTUATION = 'PUNCTUATION'  
    BEGIN = 'INDENT'  
    END = 'DEDENT'  
    EOF = 'EOF' 
    STRING = 'STRING'  
    UNKNOWN = 'UNKNOWN'  
    NEWLINE = 'NEWLINE' 

    # Méthode pour vérifier si un token est un opérateur binaire
    @classmethod
    def is_binary_operator(cls, token):
        # Liste des opérateurs binaires possibles avec leur type
        binaires = {
            '&&': 'LOGICAL_AND',
            '||': 'LOGICAL_OR',
            '==': 'EQUAL',
            '!=': 'NOT_EQUAL',
            '<=': 'LESS_EQUAL',
            '>=': 'GREATER_EQUAL',
            '++': 'INCREMENT',
            '--': 'DECREMENT',
            '//': 'FLOOR_DIV',
            '<<': 'SHIFT_LEFT',
            '>>': 'SHIFT_RIGHT',
            '**': 'POWER',
            '-=': 'SUBTRACT',
            '+=': 'ADD',
            '*=': 'MULTIPLY'
        }
        return binaires.get(token, None)

    # Méthode pour vérifier si un token est un opérateur unaire
    @classmethod
    def is_unary_operator(cls, token):
        unaires = {
            '+': 'PLUS',
            '-': 'MINUS',
            '!': 'NOT',
            '~': 'BITWISE_NOT',
            '=': 'EQUAL',
            '*': 'PRODUCT',
            '/': 'DIV',
            '%': 'MOD',
            '>': 'GREATER',
            '<': 'LESS'
        }
        return unaires.get(token, None)

# Classe de base pour tous les tokens
class BaseToken:
    def __init__(self, type_, value, line, column):
        self.type = type_  
        self.value = value  
        self.line = line  
        self.column = column  

    def __repr__(self):
        # Représentation du token pour faciliter le débogage
        return f'{self.type.name}({self.value}) at line {self.line}, column {self.column}'

    # Méthode utilisée dans l'analyse syntaxique pour représenter un token
    def analyse_syntaxique(self):
        if self.type == TokenType.IDENTIFIER:
            return 'ident'
        elif self.type == TokenType.NUMBER:
            return 'integer'
        elif self.type in {TokenType.OPERATOR_BINARY, TokenType.OPERATOR_UNARY}:
            return self.value
        elif self.type == TokenType.KEYWORD:
            return self.value
        elif self.type == TokenType.PUNCTUATION:
            return self.value
        elif self.type == TokenType.STRING:
            return 'string'
        elif self.type == TokenType.NEWLINE:
            return 'NEWLINE'
        elif self.type == TokenType.BEGIN:
            return 'BEGIN'
        elif self.type == TokenType.END:
            return 'END'
        elif self.type == TokenType.UNKNOWN:
            return 'unknown'
        else:
            return None

# Classes spécifiques pour chaque type de token
class KeywordToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.KEYWORD, value, line, column)

class OperatorToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR, value, line, column)

class LiteralToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.NUMBER, value, line, column)

# Ajoutez des commentaires similaires pour les autres classes de tokens...

# Classes d'exception pour la gestion des erreurs lexicales
class ZeroException(Exception):
    # Levée lorsqu'un nombre commence par un zéro non autorisé
    def __init__(self, ligne, number):
        super().__init__(f"Line {ligne} : Number \"{number}\" cannot begin with 0")

class AlphainNumberException(Exception):
    # Levée lorsqu'un nombre contient des lettres non autorisées
    def __init__(self, ligne, number):
        super().__init__(f"Line {ligne} : There cannot be letters in numbers \"{number}\"")

class UnknowCaractersInVariable(Exception):
    # Levée lorsqu'une variable contient des caractères inconnus
    def __init__(self, ligne, variable):
        super().__init__(f"Line {ligne} : There cannot be unknow caracters in identifiers in {variable}")

class IndentException(Exception):
    # Levée lorsqu'il y a une erreur d'indentation
    def __init__(self, ligne):
        super().__init__(f"Line {ligne} : indentation error")
