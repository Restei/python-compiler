from enum import Enum


class TokenType(Enum):
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
    
    @classmethod
    def is_binary_operator(cls, token):
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



class BaseToken:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'{self.type.name}({self.value}) at line {self.line}, column {self.column}'


class KeywordToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.KEYWORD, value, line, column)

class OperatorToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR, value, line, column)

class LiteralToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.NUMBER, value, line, column)

class IdentifierToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.IDENTIFIER, value, line, column)

class PunctuationToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.PUNCTUATION, value, line, column)

class IndentToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.BEGIN, '', line, column)

class DedentToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.END, '', line, column)

class OperatorUnaryToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR_UNARY, value, line, column)

class OperatorBinaryToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR_BINARY, value, line, column)

class NewlineToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.NEWLINE, '' , line, column)

class UnknownToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.UNKNOWN, value, line, column)

class StringToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.STRING, value, line, column)

class ZeroException(Exception):
    def __init__(self,ligne):
        super().__init__(f"Line {ligne} : Number cannot begin with 0")

class AlphainNumberException(Exception):
    def __init__(self,ligne):
        super().__init__(f"Line {ligne} : There cannot be letters in numbers")