from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    KEYWORD = 'KEYWORD'
    OPERATOR_UNARY = 'OPERATOR_UNARY'
    OPERATOR_BINARY = 'OPERATOR_BINARY'
    PUNCTUATION = 'PUNCTUATION'
    INDENT = 'INDENT'
    DEDENT = 'DEDENT'
    NEWLINE = 'NEWLINE'
    EOF = 'EOF'

    
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
            '**': 'POWER'
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
            '/': 'DIV'
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

class NewlineToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.NEWLINE, '\\n', line, column)

class IndentToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.INDENT, 'INDENT', line, column)

class DedentToken(BaseToken):
    def __init__(self, line, column):
        super().__init__(TokenType.DEDENT, 'DEDENT', line, column)

class OperatorUnaryToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR_UNARY, value, line, column)

class OperatorBinaryToken(BaseToken):
    def __init__(self, value, line, column):
        super().__init__(TokenType.OPERATOR_BINARY, value, line, column)

