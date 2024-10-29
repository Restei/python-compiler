# Ce script servira à introduire et définir les différents Tokens dans lee cadre de l'analyse lexicale 

from enum import auto, Enum

class TokenType(Enum):
    # Mots-clés
    IF = auto()  # 'if'
    ELIF = auto()  # 'elif'
    ELSE = auto()  # 'else'
    FOR = auto()  # 'for'
    WHILE = auto()  # 'while'
    DEF = auto()  # 'def'
    CLASS = auto()  # 'class'
    IMPORT = auto()  # 'import'
    FROM = auto()  # 'from'
    RETURN = auto()  # 'return'
    BREAK = auto()  # 'break'
    CONTINUE = auto()  # 'continue'
    PASS = auto()  # 'pass'
    TRUE = auto()  # 'True'
    FALSE = auto()  # 'False'
    
    # Opérateurs
    PLUS = auto()  # '+'
    MINUS = auto()  # '-'
    MULTIPLY = auto()  # '*'
    DIVIDE = auto()  # '/'
    MODULO = auto()  # '%'
    POWER = auto()  # '**'
    INCREMENT = auto()  # '++'
    DECREMENT = auto()  # '--'
    
    # Opérateurs de comparaison
    EQUAL = auto()  # '=='
    NOT_EQUAL = auto()  # '!='
    LESS_THAN = auto()  # '<'
    GREATER_THAN = auto()  # '>'
    LESS_EQUAL = auto()  # '<='
    GREATER_EQUAL = auto()  # '>='
    
    # Opérateurs logiques
    AND = auto()  # '&&'
    OR = auto()  # '||'
    NOT = auto()  # '!'
    
    # Autres symboles
    ASSIGN = auto()  # '='
    OPEN_PAREN = auto()  # '('
    CLOSE_PAREN = auto()  # ')'
    COMMA = auto()  # ','
    COLON = auto()  # ':'
    NEWLINE = auto()  # '\n'
    INDENT = auto()  # indentation
    DEDENT = auto()  # dé-dent
    
    # Types de données
    IDENTIFIER = auto()  # Variable ou nom d'identifiant
    NUMBER = auto()  # Un nombre (entier ou flottant)
    STRING = auto()  # Une chaîne de caractères
    
    # Fin du fichier
    EOF = auto()  # End Of File

    # Classe de base pour un Token
class BaseToken:
    def __init__(self, token_type: TokenType, value: str, ligne: int, colonne: int):
        self.token_type = token_type  # Type du token (ex. KEYWORD, OPERATOR)
        self.value = value  # Valeur du token (texte du token)
        self.ligne = ligne  # Ligne où le token a été trouvé
        self.colonne = colonne  # Colonne où le token a été trouvé

    def __repr__(self):
        return f"{self.__class__.__name__}(Type: {self.token_type.name}, Value: {repr(self.value)}, Ligne: {self.ligne}, Colonne: {self.colonne})"


# Classe pour les mots-clés (ex. if, else, for)
class KeywordToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.KEYWORD, value, ligne, colonne)


# Classe pour les opérateurs (ex. +, -, ==)
class OperatorToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.OPERATOR, value, ligne, colonne)


# Classe pour les littéraux comme les nombres ou chaînes de caractères
class LiteralToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.LITERAL, value, ligne, colonne)


# Classe pour les identifiants (ex. noms de variables, fonctions)
class IdentifierToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.IDENTIFIER, value, ligne, colonne)


# Classe pour la ponctuation (ex. , ; ( ))
class PunctuationToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.PUNCTUATION, value, ligne, colonne)


# Classe pour les tokens spéciaux (ex. saut de ligne, indentation, etc.)
class SpecialToken(BaseToken):
    def __init__(self, value: str, ligne: int, colonne: int):
        super().__init__(TokenType.SPECIAL, value, ligne, colonne)

# Exemple de classes dérivées de SpecialToken pour des cas spécifiques
class NewlineToken(SpecialToken):
    def __init__(self, ligne: int, colonne: int):
        super().__init__('\\n', ligne, colonne)

class IndentToken(SpecialToken):
    def __init__(self, ligne: int, colonne: int):
        super().__init__('INDENT', ligne, colonne)

class DedentToken(SpecialToken):
    def __init__(self, ligne: int, colonne: int):
        super().__init__('DEDENT', ligne, colonne)

# Ce fichier définit différentes classes pour représenter les tokens dans un analyseur lexical.
# Il repose sur une hiérarchie claire de classes pour encapsuler différents types de tokens.

# 1. `TokenType` est une énumération (Enum) qui liste les types génériques de tokens.
#    Chaque type de token est associé à une catégorie (mots-clés, opérateurs, littéraux, etc.).
#    Cette énumération utilise `auto()` pour générer automatiquement les valeurs de chaque type,
#    ce qui permet une évolution plus facile du code sans avoir à assigner manuellement des valeurs constantes.

# 2. `BaseToken` est la classe de base pour tous les tokens. Elle prend en entrée :
#    - `token_type` : Un type issu de `TokenType`, qui détermine la catégorie du token.
#    - `value` : La valeur réelle du token, c'est-à-dire le texte capturé par l'analyse lexicale (ex : "if", "42", "+").
#    - `ligne` et `colonne` : Les coordonnées du token dans le texte source (ligne et colonne).
#    Cette classe définit également une méthode `__repr__` qui formate l'affichage du token 
#    pour le débogage ou la lecture humaine. Cela permet de visualiser rapidement de quel type est le token,
#    quelle est sa valeur, et où il se trouve dans le fichier source.

# 3. Les classes dérivées de `BaseToken` :
#    - Chaque type de token est représenté par une sous-classe spécialisée de `BaseToken`, héritant des attributs
#      et méthodes de `BaseToken`. Cela permet d'étendre ou de modifier facilement le comportement pour chaque type
#      de token, si nécessaire.
#    
#    3.1. `KeywordToken` : Spécialise `BaseToken` pour les mots-clés du langage (comme `if`, `else`, `while`).
#         Ce type de token est associé à `TokenType.KEYWORD` et représente les instructions du langage de programmation.
#         Exemple : `KeywordToken("if", 1, 0)` représente le mot-clé `if` trouvé à la première ligne, première colonne.

#    3.2. `OperatorToken` : Cette classe est utilisée pour les opérateurs (comme `+`, `-`, `==`).
#         L'analyse lexicale reconnaît ces symboles comme des opérateurs et crée un objet `OperatorToken`
#         avec `TokenType.OPERATOR`. Exemple : `OperatorToken("==", 1, 3)` pour l'opérateur `==` à la ligne 1, colonne 3.

#    3.3. `LiteralToken` : Représente les littéraux, comme les nombres ou les chaînes de caractères.
#         Les littéraux sont des valeurs directes dans le code source, comme `42` pour un entier, ou `"Hello"` pour une chaîne.
#         Exemple : `LiteralToken("42", 1, 15)` représente le nombre `42` trouvé à la ligne 1, colonne 15.

#    3.4. `IdentifierToken` : Utilisé pour les identifiants (comme les noms de variables, de fonctions ou de classes).
#         Un identifiant est un nom donné par le programmeur pour référencer une entité dans le programme (comme une variable).
#         Exemple : `IdentifierToken("variable", 1, 6)` représente l'identifiant `variable` à la ligne 1, colonne 6.

#    3.5. `PunctuationToken` : Représente les caractères de ponctuation tels que `,`, `;`, `(`, `)`, etc.
#         Ce type de token est utilisé pour tous les symboles qui servent à la structure du code (parenthèses, virgules, etc.).
#         Exemple : `PunctuationToken("(", 1, 13)` représente une parenthèse ouvrante trouvée à la ligne 1, colonne 13.

#    3.6. `SpecialToken` : Représente des tokens spéciaux qui ne rentrent pas dans les catégories précédentes.
#         Cela inclut les retours à la ligne (`\n`), les indentations (`INDENT`), les dé-dentations (`DEDENT`), ou encore
#         les commentaires. Les classes dérivées comme `NewlineToken`, `IndentToken` et `DedentToken` permettent de
#         capturer ces événements spéciaux dans l'analyse lexicale.

# 4. `__repr__` dans chaque classe dérivée :
#    Chaque classe hérite de la méthode `__repr__` de la classe `BaseToken`, ce qui permet d'afficher
#    une représentation lisible et utile des tokens pour les tests et le débogage.
#    Cela produit une chaîne de caractères de la forme : `Token(Type: KEYWORD, Value: 'if', Ligne: 1, Colonne: 0)`
#    où le type de token, sa valeur et sa position dans le fichier source sont clairement indiqués.
