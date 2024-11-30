from analyse_syntaxique.GrammaireLL1 import *
from analyse_lexicale.fonction_lexicale import Lexeur  # Importer le lexeur pour transformer le code source en tokens
from analyse_lexicale.fonction_lexicale import TokenType  # Importer les types de tokens et exceptions


class LL1Parser:
    """
    Classe pour un analyseur syntaxique LL(1).
    Transforme une liste de tokens en une structure syntaxique, tout en vérifiant
    que le code respecte la grammaire définie.
    """

    def __init__(self, source_code):
        """
        Initialisation du parseur.
        1. Analyse lexicale : Transforme le code source brut en tokens.
        2. Prépare les tokens pour l'analyse syntaxique.
        
        :param source_code: Le code source à analyser.
        """
        # Étape 1 : Analyse lexicale
        lexeur = Lexeur(source_code)  # Instancie le lexeur avec le code source donné
        self.tokens, self.errors = lexeur.Tokenisation()  # Génére les tokens et capture les erreurs lexicales

        # Si des erreurs lexicales sont détectées, les afficher et arrêter l'exécution
        if self.errors:
            for error in self.errors:
                print(f"Erreur lexicale : {error}")  # Affiche chaque erreur lexicale
            raise Exception("Analyse lexicale échouée. Veuillez corriger les erreurs dans le code source.")  # Interrompt l'exécution

        # Étape 2 : Préparation pour l'analyse syntaxique
        self.current_index = 0  # Position actuelle dans la liste des tokens
        self.current_token = self.tokens[0] if self.tokens else None  # Initialise avec le premier token, ou None si la liste est vide

    def avancer(self):
        """
        Passe au token suivant dans la liste.
        Met à jour `self.current_token` avec le prochain token.
        """
        self.current_index += 1  # Incrémente l'index du token courant
        if self.current_index < len(self.tokens):  # Si l'index est valide
            self.current_token = self.tokens[self.current_index]  # Met à jour le token courant
        else:
            self.current_token = None  # Sinon, on atteint la fin des tokens (EOF)

    def consommer(self, token_type):
        """
        Vérifie si le token courant correspond au type attendu.
        Si oui, avance vers le token suivant. Sinon, lève une exception.

        :param token_type: Type de token attendu (ex: TokenType.KEYWORD, TokenType.IDENTIFIER).
        """
        if self.current_token and self.current_token.type == token_type:
            self.avancer()  # Passe au prochain token
        else:
            # Lève une exception si le token courant ne correspond pas à ce qui est attendu
            raise UnexpectedTokenError(
                token_type,  # Type de token attendu
                self.current_token.type if self.current_token else 'EOF',  # Type du token trouvé (ou EOF si fin de fichier)
                self.current_token.line if self.current_token else -1,  # Ligne du token courant (ou -1 si EOF)
                self.current_token.column if self.current_token else -1  # Colonne du token courant (ou -1 si EOF)
            )

    def parse(self):
        """
        Point d'entrée principal pour l'analyse syntaxique.
        Appelle la règle principale de la grammaire (`file`).
        """
        try:
            self.file()  # Commence l'analyse avec la règle `file`
            print("Analyse syntaxique réussie. Aucun problème détecté.")  # Message en cas de succès
        except LL1SyntaxException as e:
            # Capture et affiche toute erreur de syntaxe
            print(f"Erreur de syntaxe : {e}")
            raise 

    def file(self):
        """
        Règle : file → NEWLINE <defetoile> <stmt> <stmtetoile> EOF
        Vérifie la structure globale du fichier, incluant :
        - Une ligne vide (NEWLINE)
        - Zéro ou plusieurs déclarations de fonctions (<defetoile>)
        - Une ou plusieurs instructions (<stmt> et <stmtetoile>)
        - Fin de fichier (EOF)
        """
        if not self.current_token:
            # Si aucun token n'est présent, lève une exception EOF inattendu
            raise UnexpectedEOFError(-1, -1)
        try:
            self.consommer(TokenType.NEWLINE)  # Vérifie et consomme un NEWLINE initial
            self.defetoile()  # Analyse toutes les déclarations de fonctions éventuelles
            self.stmt()  # Analyse la première instruction
            self.stmtetoile()  # Analyse les instructions supplémentaires
            self.consommer(TokenType.EOF)  # Vérifie que le fichier se termine correctement
        except UnexpectedTokenError:
            # Si un token inattendu est trouvé, lève une erreur de structure
            raise FileStructureError(self.current_token.line, self.current_token.column)

    def defetoile(self):
        """
        Règle : defetoile → <def> <defetoile> | ε
        Cette règle gère une liste (ou absence) de déclarations de fonctions.
        """
        while self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'def':
            self.def_rule()  # Analyse une déclaration de fonction

    def stmtetoile(self):
        """
        Règle : stmtetoile → <stmt> <stmtetoile> | ε
        Cette règle gère une liste d'instructions.
        """
        while self.current_token and self.current_token.type in [TokenType.IDENTIFIER, TokenType.KEYWORD]:
            self.stmt()  # Analyse une instruction

    def def_rule(self):
        """
        Règle : def → def IDENTIFIER ( <arg> ) : <suite>
        Analyse une déclaration de fonction avec :
        - Le mot-clé `def`
        - Un identifiant (nom de la fonction)
        - Une liste d'arguments entre parenthèses
        - Un deux-points suivi d'un bloc de code (suite)
        """
        try:
            self.consommer(TokenType.KEYWORD)  # Vérifie et consomme le mot-clé `def`
            self.consommer(TokenType.IDENTIFIER)  # Vérifie et consomme le nom de la fonction
            self.consommer(TokenType.PUNCTUATION)  # Consomme '('
            self.arg()  # Analyse les arguments de la fonction
            self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
            self.consommer(TokenType.PUNCTUATION)  # Consomme ':'
            self.suite()  # Analyse le bloc de code de la fonction
        except UnexpectedTokenError:
            # Lève une erreur si la déclaration de fonction est incorrecte
            raise FunctionDefinitionError(self.current_token.line, self.current_token.column)

    def arg(self):
        """
        Règle : arg → IDENTIFIER <nextarg> | ε
        Analyse une liste d'arguments (ou rien).
        """
        if self.current_token.type == TokenType.IDENTIFIER:
            self.consommer(TokenType.IDENTIFIER)  # Consomme le premier argument
            self.nextarg()  # Vérifie s'il y a des arguments supplémentaires
        elif self.current_token.type not in [TokenType.PUNCTUATION]:
            # Si aucun argument n'est trouvé mais un token inattendu est présent
            raise ArgumentListError(self.current_token.line, self.current_token.column)

    def nextarg(self):
        """
        Règle : nextarg → , IDENTIFIER <nextarg> | ε
        Gère les arguments supplémentaires séparés par des virgules.
        """
        while self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
            self.consommer(TokenType.PUNCTUATION)  # Consomme la virgule
            self.consommer(TokenType.IDENTIFIER)  # Consomme l'argument suivant

    def suite(self):
        """
        Règle : suite → NEWLINE BEGIN <stmt> <stmtetoile> END
        Analyse un bloc de code indenté.
        """
        try:
            self.consommer(TokenType.NEWLINE)  # Consomme un NEWLINE
            self.consommer(TokenType.BEGIN)  # Vérifie le début d'un bloc indenté
            self.stmt()  # Analyse la première instruction du bloc
            self.stmtetoile()  # Analyse les instructions supplémentaires
            self.consommer(TokenType.END)  # Vérifie la fin du bloc indenté
        except UnexpectedTokenError:
            # Lève une exception si le bloc est mal formé
            raise SuiteBlockError(self.current_token.line, self.current_token.column)

    def stmt(self):
        """
        Règle : stmt → <simplestmt> NEWLINE | if <exprinit> : <suite> <else>
        Analyse une instruction :
        - Une instruction simple suivie d'un NEWLINE
        - Une condition `if` avec éventuellement un `else`.
        """
        if not self.current_token:
            # Lève une erreur si aucun token n'est disponible
            raise UnexpectedEOFError(self.current_token.line if self.current_token else -1, 
                                    self.current_token.column if self.current_token else -1)

        try:
            # Cas 1 : Une condition `if`
            if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'if':
                self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `if`
                self.exprinit()  # Analyse l'expression conditionnelle
                self.consommer(TokenType.PUNCTUATION)  # Consomme le `:`
                self.suite()  # Analyse le bloc de code associé au `if`
                self.else_rule()  # Analyse l'éventuelle clause `else`

            # Cas 2 : Une instruction simple (comme un `print`)
            elif self.current_token.type in [TokenType.KEYWORD, TokenType.IDENTIFIER]:
                self.simplestmt()  # Analyse une instruction simple
                self.consommer(TokenType.NEWLINE)  # Vérifie et consomme le NEWLINE final

            else:
                # Cas par défaut : Token inattendu pour une instruction
                raise SimpleStatementError(
                    self.current_token.line, self.current_token.column
                )
        except UnexpectedTokenError as e:
            # Capture et relance l'erreur pour une meilleure traçabilité
            raise SyntaxError(f"Erreur dans l'instruction à la ligne {e.line}, colonne {e.column}: {e.message}")


    def else_rule(self):
        """
        Règle : else → else : <suite> | ε
        Analyse une clause `else`, si elle est présente.
        """
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'else':
            self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `else`
            self.consommer(TokenType.PUNCTUATION)  # Consomme ':'
            self.suite()  # Analyse le bloc de code associé au `else`

    def simplestmt(self):
        """
        Règle : simplestmt → return <exprinit> | print ( <exprinit> )
                | IDENTIFIER <simplestmtident> | <exprinit>
        Analyse une instruction simple comme un `return`, un `print`, ou une expression.
        """
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'return':
            self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `return`
            self.exprinit()  # Analyse l'expression qui suit
        elif self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'print':
            self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `print`
            self.consommer(TokenType.PUNCTUATION)  # Consomme '('
            self.exprinit()  # Analyse l'expression dans `print`
            self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
        elif self.current_token.type == TokenType.IDENTIFIER:
            self.consommer(TokenType.IDENTIFIER)  # Consomme l'identifiant
            self.simplestmtident()  # Vérifie s'il y a une affectation
        else:
            self.exprinit()  # Analyse une expression autonome

    def simplestmtident(self):
        """
        Règle : simplestmtident → = <exprinit> | ε
        Vérifie une éventuelle affectation après un identifiant.
        """
        if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '=':
            self.consommer(TokenType.PUNCTUATION)  # Consomme '='
            self.exprinit()  # Analyse l'expression assignée

    def exprinit(self):
        """
        Règle : exprinit → <expr> <exprdroit>
        Analyse une expression initiale suivie éventuellement d'un opérateur binaire.
        """
        self.expr()  # Analyse la partie gauche de l'expression
        self.exprdroit()  # Vérifie s'il y a une continuation

    def expr(self):
        """
         Règle : expr → UnaryOp <expr> | CONST | not <expr> | <exprprime>
        Analyse une constante, un opérateur unaire, une négation ou une expression primaire.
        """
        if self.current_token.type in [TokenType.NUMBER, TokenType.STRING]:
            # Cas 1 : Constante (nombre ou chaîne de caractères)
            self.consommer(self.current_token.type)  # Consomme le token (CONST)
    
        elif self.current_token.type == TokenType.OPERATOR_UNARY:
        # Cas 2 : Opérateur unaire (comme +, -)
            self.consommer(TokenType.OPERATOR_UNARY)  # Consomme l'opérateur unaire
            self.expr()  # Analyse l'expression qui suit l'opérateur
    
        elif self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'not':
        # Cas 3 : Négation logique
            self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `not`
            self.expr()  # Analyse l'expression qui suit
    
        else:
        # Cas 4 : Expression primaire
            self.exprprime()  # Appel pour analyser une expression primaire


    def exprprime(self):
        """
        Règle : exprprime → IDENTIFIER | ( <expr> ) | [ <expr> ]
        Analyse un identifiant, une expression entre parenthèses ou une liste.
        """
        if self.current_token.type == TokenType.IDENTIFIER:
            self.consommer(TokenType.IDENTIFIER)  # Consomme un identifiant
        elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '(':
            self.consommer(TokenType.PUNCTUATION)  # Consomme '('
            self.expr()  # Analyse l'expression entre parenthèses
            self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
        elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '[':
            self.consommer(TokenType.PUNCTUATION)  # Consomme '['
            self.expr()  # Analyse l'expression dans la liste
            self.consommer(TokenType.PUNCTUATION)  # Consomme ']'
        else:
            # Lève une erreur si le format d'expression est incorrect
            raise ExpressionError(self.current_token.line, self.current_token.column)

    def exprdroit(self):
        """
        Règle : exprdroit → BINOP <exprinit> | ε
        Analyse une continuation d'expression après un opérateur binaire.
        """
        if self.current_token.type == TokenType.OPERATOR_BINARY:
            self.consommer(TokenType.OPERATOR_BINARY)  # Consomme un opérateur binaire
            self.exprinit()  # Analyse la partie droite de l'expression
