from analyse_syntaxique.GrammairesLL1 import *
from analyse_lexicale.fonction_lexicale import Lexeur  # Importer le lexeur pour transformer le code source en tokens
from analyse_lexicale.token import TokenType  # Importer les types de tokens et exceptions
from analyse_syntaxique.arbre import *

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
        self.tokens, self.lexical_errors = lexeur.Tokenisation()  # Génére les tokens et capture les erreurs lexicales

        # Liste pour enregistrer les erreurs syntaxiques
        self.errors = []  # Collecte toutes les erreurs syntaxiques détectées

        # Si des erreurs lexicales sont détectées, les afficher
        if self.lexical_errors:
            for error in self.lexical_errors:
                print(f"Erreur lexicale : {error}")  # Affiche chaque erreur lexicale
            raise Exception("Analyse lexicale échouée. Veuillez corriger les erreurs dans le code source.")  # Interrompt l'exécution

        # Étape 2 : Préparation pour l'analyse syntaxique
        self.current_index = 0  # Position actuelle dans la liste des tokens
        self.current_token = self.tokens[0] if self.tokens else None  # Initialise avec le premier token, ou None si la liste est vide

        self.ast = None  # Arbre syntaxique abstrait, initialisé à None
        
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

    def detecter_erreurs(self, exception):
        """
        Ajoute une erreur à la liste des erreurs syntaxiques détectées.
        Permet de capturer les erreurs sans arrêter immédiatement l'analyse.

        :param exception: L'exception qui décrit l'erreur détectée.
        """
        self.errors.append(exception)  # Ajoute l'erreur à la liste
        print(f"Erreur détectée : {exception}")  # Affiche l'erreur pour information

    def parse(self):
        """
        Point d'entrée principal pour l'analyse syntaxique.
        Appelle la règle principale de la grammaire (`file`).
        """
        try:
            self.file()  # Commence l'analyse avec la règle `file`
        except Exception as e:
            self.detecter_erreurs(e)  # Capture une erreur inattendue
        finally:
            # Affiche toutes les erreurs collectées après l'analyse
            if self.errors:
                print("\nAnalyse syntaxique terminée avec des erreurs :")
                for error in self.errors:
                    print(f"  - {error}")
            else:
                print("\nAnalyse syntaxique réussie. Aucun problème détecté.")

    def file(self):
        """
        Règle : file → NEWLINE <defetoile> <stmt> <stmtetoile> EOF
        Vérifie la structure globale du fichier.
        """
        node = Node("file")
        try:
            self.consommer(TokenType.NEWLINE)  # Consomme un NEWLINE initial
            self.defetoile()  # Analyse les déclarations de fonctions éventuelles
            self.stmt()  # Analyse la première instruction
            self.stmtetoile()  # Analyse les instructions supplémentaires
            self.consommer(TokenType.EOF)  # Vérifie que le fichier se termine correctement
            node.ajouter_fils_noeud(self.defetoile())
            node.ajouter_fils_noeud(self.stmt())
            node.ajouter_fils_noeud(self.stmtetoile())
        except UnexpectedTokenError as e:
            self.detecter_erreurs(FileStructureError(self.current_token.line, self.current_token.column))
        return node
    
    def defetoile(self):
        """
        Règle : defetoile → <def> <defetoile> | ε
        Analyse une série de déclarations de fonctions, ou rien.
        """
        node = Node("defetoile")
        while self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'def':
            try:
                self.def_rule()
                node.ajouter_fils_noeud(self.def_rule())
            except FunctionDefinitionError as e:
                self.detecter_erreurs(e)
            return node
    
    
    def stmtetoile(self):
        """
        Règle : stmtetoile → <stmt> <stmtetoile> | ε
        Analyse une série d'instructions, ou rien.
        """
        node = Node("stmtetoile")
        while self.current_token and self.current_token.type in [TokenType.IDENTIFIER, TokenType.KEYWORD]:
            try:
                self.stmt()
                node.ajouter_fils_noeud(self.stmt())
            except SimpleStatementError as e:
                self.detecter_erreurs(e)
            return node
        
    def def_rule(self):
        """
        Règle : def → def IDENTIFIER ( <arg> ) : <suite>
        Analyse une déclaration de fonction complète.
        """
        node = Node("def")
        try:
            self.consommer(TokenType.KEYWORD)  # Vérifie le mot-clé `def`
            node.ajouter_fils(self.current_token.value)
            self.consommer(TokenType.IDENTIFIER)  # Vérifie le nom de la fonction
            self.consommer(TokenType.PUNCTUATION)  # Consomme '('
            self.arg()  # Analyse les arguments de la fonction
            node.ajouter_fils_noeud(self.arg())
            self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
            self.consommer(TokenType.PUNCTUATION)  # Consomme ':'
            self.suite()  # Analyse le bloc de code
            node.ajouter_fils_noeud(self.suite())
        except UnexpectedTokenError as e:
            raise FunctionDefinitionError(self.current_token.line, self.current_token.column) from e
        return node
    
    def arg(self):
        """
        Règle : arg → IDENTIFIER <nextarg> | ε
        Analyse une liste d'arguments (ou rien).
        """
        node = Node("arg")
        try:
            if self.current_token.type == TokenType.IDENTIFIER:
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.IDENTIFIER)  # Consomme le premier argument
                self.nextarg()  # Vérifie s'il y a des arguments supplémentaires
                node.ajouter_fils_noeud(self.nextarg())
        except UnexpectedTokenError as e:
            raise ArgumentListError(self.current_token.line, self.current_token.column) from e
        return node
    def nextarg(self):
        """
        Règle : nextarg → , IDENTIFIER <nextarg> | ε
        Gère les arguments supplémentaires séparés par des virgules.
        """
        node = Node("nextarg")
        while self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == ',':
            try:
                self.consommer(TokenType.PUNCTUATION)  # Consomme la virgule
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.IDENTIFIER)  # Consomme l'argument suivant
            except UnexpectedTokenError as e:
                raise ArgumentListError(self.current_token.line, self.current_token.column) from e
            return node
        
    def suite(self):
        """
        Règle : suite → NEWLINE BEGIN <stmt> <stmtetoile> END
        Analyse un bloc de code indenté.
        """
        node = Node("suite")
        try:
            self.consommer(TokenType.NEWLINE)  # Consomme un NEWLINE
            self.consommer(TokenType.BEGIN)  # Vérifie le début du bloc indenté
            self.stmt()  # Analyse la première instruction du bloc
            self.stmtetoile()  # Analyse les instructions suivantes
            self.consommer(TokenType.END)  # Vérifie la fin du bloc indenté
            node.ajouter_fils_noeud(self.stmt())
            node.ajouter_fils_noeud(self.stmtetoile())
        except UnexpectedTokenError as e:
            raise SuiteBlockError(self.current_token.line, self.current_token.column) from e
        return node
    
    def stmt(self):
        """
        Règle : stmt → <simplestmt> NEWLINE | if <exprinit> : <suite> <else>
        Analyse une instruction.
        """
        node = Node("stmt")
        try:
            if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'if':
                self.consommer(TokenType.KEYWORD)  # Vérifie le mot-clé `if`
                self.exprinit()  # Analyse l'expression conditionnelle
                node.ajouter_fils_noeud(self.exprinit())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ':'
                self.suite()  # Analyse le bloc conditionnel
                self.else_rule()  # Analyse la clause `else`
                node.ajouter_fils_noeud(self.suite())
                node.ajouter_fils_noeud(self.else_rule())
            elif self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'print':
                self.simplestmt()
                self.consommer(TokenType.NEWLINE)  # Vérifie le NEWLINE après une instruction simple
            else:
                raise SimpleStatementError(self.current_token.line, self.current_token.column)
        except SimpleStatementError as e:
            self.detecter_erreurs(e)
        return node
    
    def else_rule(self):
        """
        Règle : else → else : <suite> | ε
        Analyse une clause `else`, si elle est présente.
        """
        node = Node("else")
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'else':
            try:
                self.consommer(TokenType.KEYWORD)  # Vérifie le mot-clé `else`
                self.consommer(TokenType.PUNCTUATION)  # Consomme ':'
                self.suite()  # Analyse le bloc associé au `else`
                node.ajouter_fils_noeud(self.suite())
            except UnexpectedTokenError as e:
                raise SuiteBlockError(self.current_token.line, self.current_token.column) from e
            return node
        
    def simplestmt(self):
        """
        Règle : simplestmt → return <exprinit> | print ( <exprinit> )
                | IDENTIFIER <simplestmtident> | <exprinit>
        Analyse une instruction simple comme un `return`, un `print`, ou une expression.
        """
        node = Node("simplestmt")
        try: 

            if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'return':
                self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `return`
                self.exprinit()  # Analyse l'expression qui suit
                node.ajouter_fils_noeud(self.exprinit())
            elif self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'print':
                self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `print`
                self.consommer(TokenType.PUNCTUATION)  # Consomme '('
                self.exprinit()  # Analyse l'expression dans `print`
                node.ajouter_fils_noeud(self.exprinit())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
            elif self.current_token.type == TokenType.IDENTIFIER:
                self.consommer(TokenType.IDENTIFIER)  # Consomme l'identifiant
                self.simplestmtident()  # Vérifie s'il y a une affectation
                node.ajouter_fils_noeud(self.simplestmtident())
            else:
                self.exprinit()  # Analyse une expression autonome
                node.ajouter_fils_noeud(self.exprinit())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node 
    
    def simplestmtident(self):
        """
        Règle : simplestmtident → = <exprinit> | ε
        Vérifie une éventuelle affectation après un identifiant.
        """
        node = Node("simplestmtident")
        try: 
            if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '=':
                self.consommer(TokenType.PUNCTUATION)  # Consomme '='
                self.exprinit()  # Analyse l'expression assignée
                node.ajouter_fils_noeud(self.exprinit())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def exprinit(self):
        """
        Règle : exprinit → <expr> <exprdroit>
        Analyse une expression initiale suivie éventuellement d'un opérateur binaire.
        """
        node = Node("exprinit")
        try:
            self.expr()  # Analyse la partie gauche de l'expression
            self.exprdroit()  # Vérifie s'il y a une continuation
            node.ajouter_fils_noeud(self.expr())
            node.ajouter_fils_noeud(self.exprdroit())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node
    
    def expr(self):
        """
        Règle : expr → CONST | not <expr> | <exprprime>
        Analyse une constante, une négation, ou une expression primaire.
        """
        node = Node("expr")
        try:
            if self.current_token.type in [TokenType.NUMBER, TokenType.STRING]:
                node.ajouter_fils(self.current_token.value)
                self.consommer(self.current_token.type)  # Consomme un nombre ou une chaîne
            elif self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'not':
                self.consommer(TokenType.KEYWORD)  # Consomme le mot-clé `not`
                self.expr()  # Analyse l'expression qui suit
                node.ajouter_fils_noeud(self.expr())
            else:
                self.exprprime()  # Analyse une expression primaire
                node.ajouter_fils_noeud(self.exprprime())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node
    
    def exprprime(self):
        """
        Règle : exprprime → IDENTIFIER | ( <expr> ) | [ <expr> ]
        Analyse un identifiant, une expression entre parenthèses ou une liste.
        """
        node = Node("exprprime")
        try:
            if self.current_token.type == TokenType.IDENTIFIER:
                # Ajout de l'identifiant en tant que sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.IDENTIFIER)  # Consomme l'identifiant
            elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '(':
                self.consommer(TokenType.PUNCTUATION)  # Consomme '('
                # Ajout de l'expression entre parenthèses en tant que sous-nœud
                node.ajouter_fils_noeud(self.expr())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
            elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '[':
                self.consommer(TokenType.PUNCTUATION)  # Consomme '['
                # Ajout de l'expression dans la liste en tant que sous-nœud
                node.ajouter_fils_noeud(self.expr())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ']'
            else:
                raise ExpressionError(self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def exprdroit(self):
        """
        Règle : exprdroit → BINOP <exprinit> | ε
        Analyse une continuation d'expression après un opérateur binaire.
        """
        node = Node("exprdroit")
        try:
            if self.current_token.type == TokenType.BINOP:
                # Ajout de l'opérateur binaire comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.BINOP)  # Consomme l'opérateur binaire
                # Ajout de l'expression droite comme sous-nœud
                node.ajouter_fils_noeud(self.exprinit())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def binop_and(self):
        """
        Règle : binopAnd → and <binopAndEtoile>
        """
        node = Node("binopAnd")
        try:
            while self.current_token.value == "and":
                # Ajout de l'opérateur `and` comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.BINOP)  # Consomme `and`
                # Ajout des sous-expressions liées à `and` comme sous-nœud
                node.ajouter_fils_noeud(self.binop_and_etoile())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def binop_and_etoile(self):
        """
        Règle : binopAndEtoile → <expr> <binopAndEtoile> | ε
        """
        node = Node("binopAndEtoile")
        try:
            if self.current_token.type in [TokenType.NUMBER, TokenType.IDENTIFIER]:
                # Ajout de l'expression comme sous-nœud
                node.ajouter_fils_noeud(self.expr())
                # Ajout de la récursion (suite des opérateurs `and`) comme sous-nœud
                node.ajouter_fils_noeud(self.binop_and_etoile())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def binop_or(self):
        """
        Règle : binopOr → or <binopOrEtoile>
        """
        node = Node("binopOr")
        try:
            while self.current_token.value == "or":
                # Ajout de l'opérateur `or` comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.BINOP)  # Consomme `or`
                # Ajout des sous-expressions liées à `or` comme sous-nœud
                node.ajouter_fils_noeud(self.binop_or_etoile())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def binop_or_etoile(self):
        """
        Règle : binopOrEtoile → <expr> <binopOrEtoile> | ε
        """
        node = Node("binopOrEtoile")
        try:
            if self.current_token.type in [TokenType.NUMBER, TokenType.IDENTIFIER]:
                # Ajout de l'expression comme sous-nœud
                node.ajouter_fils_noeud(self.expr())
                # Ajout de la récursion (suite des opérateurs `or`) comme sous-nœud
                node.ajouter_fils_noeud(self.binop_or_etoile())
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def comp(self):
        """
        Règle : comp → == | != | < | > | <= | >=
        """
        node = Node("comp")
        try:
            if self.current_token.type == TokenType.OPERATOR and self.current_token.value in ['==', '!=', '<', '>', '<=', '>=']:
                # Ajout de l'opérateur de comparaison comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.OPERATOR)  # Consomme l'opérateur de comparaison
            else:
                raise ComparisonError(self.current_token.value, self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def constant(self):
        """
        Règle : const → NUMBER | STRING | True | False | None
        """
        node = Node("constant")
        try:
            if self.current_token.type in [TokenType.NUMBER, TokenType.STRING]:
                # Ajout de la constante comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(self.current_token.type)
            elif self.current_token.type == TokenType.KEYWORD and self.current_token.value in ["True", "False", "None"]:
                # Ajout de la constante booléenne ou null comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.KEYWORD)
            else:
                raise ConstantError(self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def parentheses(self):
        """
        Règle : parentheses → ( <expr> ) | [ <expr> ]
        """
        node = Node("parentheses")
        try:
            if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '(':
                self.consommer(TokenType.PUNCTUATION)  # Consomme '('
                # Ajout de l'expression entre parenthèses comme sous-nœud
                node.ajouter_fils_noeud(self.expr())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ')'
            elif self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '[':
                self.consommer(TokenType.PUNCTUATION)  # Consomme '['
                # Ajout de l'expression dans une liste comme sous-nœud
                node.ajouter_fils_noeud(self.expr())
                self.consommer(TokenType.PUNCTUATION)  # Consomme ']'
            else:
                raise ParenthesesError(self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def ident(self):
        """
        Règle : ident → <alpha> <identaux>
        Analyse un identifiant commençant par une lettre.
        """
        node = Node("ident")
        try:
            if self.current_token.type == TokenType.ALPHA:
                # Ajout du caractère initial de l'identifiant comme sous-nœud
                node.ajouter_fils(self.current_token.value)
                self.consommer(TokenType.ALPHA)
                # Ajout des suffixes de l'identifiant comme sous-nœud
                node.ajouter_fils_noeud(self.identaux())
            else:
                raise IdentifierError(self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def identaux(self):
        """
        Règle : identaux → <alpha> <identaux> | <digit> <identaux> | ε
        Analyse les suffixes d'un identifiant.
        """
        node = Node("identaux")
        try:
            while self.current_token.type in [TokenType.ALPHA, TokenType.DIGIT]:
                # Ajout des caractères supplémentaires comme sous-nœuds
                node.ajouter_fils(self.current_token.value)
                self.consommer(self.current_token.type)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def string(self):
        """
        Règle : string → " <stringaux> "
        Analyse une chaîne de caractères entourée de guillemets.
        """
        node = Node("string")
        try:
            if self.current_token.type == TokenType.PUNCTUATION and self.current_token.value == '"':
                self.consommer(TokenType.PUNCTUATION)  # Consomme le guillemet ouvrant
                # Ajout du contenu de la chaîne comme sous-nœud
                node.ajouter_fils_noeud(self.stringaux())
                self.consommer(TokenType.PUNCTUATION)  # Consomme le guillemet fermant
            else:
                raise StringError(self.current_token.line, self.current_token.column)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node

    def stringaux(self):
        """
        Règle : stringaux → <alpha> <stringaux> | <digit> <stringaux> | ε
        Analyse le contenu d'une chaîne de caractères.
        """
        node = Node("stringaux")
        try:
            while self.current_token.type in [TokenType.ALPHA, TokenType.DIGIT]:
                # Ajout des caractères alphanumériques comme sous-nœuds
                node.ajouter_fils(self.current_token.value)
                self.consommer(self.current_token.type)
        except UnexpectedTokenError as e:
            self.errors.append(e)
        return node
