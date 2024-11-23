

class LL1SyntaxException(Exception):
    """Exception générale pour les erreurs de syntaxe dans une grammaire LL(1)."""
    def __init__(self, message, line, column):
        self.line = line
        self.column = column
        super().__init__(f"{message} à la ligne {line}, colonne {column}.")

# Exceptions spécifiques aux règles de grammaire
class FileStructureError(LL1SyntaxException):
    """Erreur dans la structure globale du fichier."""
    def __init__(self, line, column):
        super().__init__("Erreur dans la structure globale du fichier", line, column)

class FunctionDefinitionError(LL1SyntaxException):
    """Erreur dans une définition de fonction (déclaration def)."""
    def __init__(self, line, column):
        super().__init__("Erreur dans la définition d'une fonction", line, column)

class ArgumentListError(LL1SyntaxException):
    """Erreur dans la liste des arguments d'une fonction."""
    def __init__(self, line, column):
        super().__init__("Erreur dans la liste des arguments", line, column)

class SuiteBlockError(LL1SyntaxException):
    """Erreur dans un bloc de suite après deux-points."""
    def __init__(self, line, column):
        super().__init__("Erreur dans un bloc de suite", line, column)

class SimpleStatementError(LL1SyntaxException):
    """Erreur dans une instruction simple."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une instruction simple", line, column)

class CompoundStatementError(LL1SyntaxException):
    """Erreur dans une instruction composée (comme if, for)."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une instruction composée", line, column)

class ExpressionError(LL1SyntaxException):
    """Erreur dans une expression."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une expression", line, column)

class ExpressionPrimeError(LL1SyntaxException):
    """Erreur dans une continuation d'expression."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une continuation d'expression", line, column)

class IdentifierExpressionError(LL1SyntaxException):
    """Erreur dans une expression contenant un identifiant."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une expression avec identifiant", line, column)

class ConstantError(LL1SyntaxException):
    """Erreur dans une constante (nombre, chaîne, etc.)."""
    def __init__(self, line, column):
        super().__init__("Erreur dans une constante", line, column)

class BinaryOperatorError(LL1SyntaxException):
    """Erreur dans l'utilisation d'un opérateur binaire."""
    def __init__(self, operator, line, column):
        super().__init__(f"Erreur dans l'opérateur binaire '{operator}'", line, column)

class IndentationError(LL1SyntaxException):
    """Erreur d'indentation (par exemple BEGIN ou END manquant)."""
    def __init__(self, line, column):
        super().__init__("Erreur d'indentation", line, column)

class UnexpectedTokenError(LL1SyntaxException):
    """Erreur pour un token inattendu lors de l'analyse LL(1)."""
    def __init__(self, expected, found, line, column):
        super().__init__(f"Token attendu '{expected}', mais trouvé '{found}'", line, column)

class UnexpectedEOFError(LL1SyntaxException):
    """Erreur pour une fin de fichier inattendue."""
    def __init__(self, line, column):
        super().__init__("Fin de fichier inattendue", line, column)