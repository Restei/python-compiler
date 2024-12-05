from analyse_lexicale.token import *

tableau_des_symboles_directeur ={
    "file": {
        "NEWLINE": "file -> NEWLINE def_etoile stmt stmt_etoile EOF",
        "def": "file -> def_etoile stmt stmt_etoile EOF",
        "IDENTIFIER": "file -> def_etoile stmt stmt_etoile EOF",
        "return": "file -> def_etoile stmt stmt_etoile EOF",
        "print": "file -> def_etoile stmt stmt_etoile EOF",
        "if": "file -> def_etoile stmt stmt_etoile EOF",
        "for": "file -> def_etoile stmt stmt_etoile EOF",
        "-": "file -> def_etoile stmt stmt_etoile EOF",
        "not": "file -> def_etoile stmt stmt_etoile EOF",
        "NUMBER": "file -> def_etoile stmt stmt_etoile EOF",
        "string": "file -> def_etoile stmt stmt_etoile EOF",
        "True": "file -> def_etoile stmt stmt_etoile EOF",
        "False": "file -> def_etoile stmt stmt_etoile EOF",
        "None": "file -> def_etoile stmt stmt_etoile EOF"
    },
    "def_etoile": {
        "def": "def_etoile -> Def def_etoile",
        "IDENTIFIER": "def_etoile -> ε",
        "return": "def_etoile -> ε",
        "print": "def_etoile -> ε",
        "if": "def_etoile -> ε",
        "for": "def_etoile -> ε",
        "-": "def_etoile -> ε",
        "not": "def_etoile -> ε",
        "NUMBER": "def_etoile -> ε",
        "string": "def_etoile -> ε",
        "True": "def_etoile -> ε",
        "False": "def_etoile -> ε",
        "None": "def_etoile -> ε"
    },
    "stmt_etoile": {
        "IDENTIFIER": "stmt_etoile -> stmt stmt_etoile",
        "return": "stmt_etoile -> stmt stmt_etoile",
        "print": "stmt_etoile -> stmt stmt_etoile",
        "if": "stmt_etoile -> stmt stmt_etoile",
        "for": "stmt_etoile -> stmt stmt_etoile",
        "-": "stmt_etoile -> stmt stmt_etoile",
        "not": "stmt_etoile -> stmt stmt_etoile",
        "NUMBER": "stmt_etoile -> stmt stmt_etoile",
        "string": "stmt_etoile -> stmt stmt_etoile",
        "True": "stmt_etoile -> stmt stmt_etoile",
        "False": "stmt_etoile -> stmt stmt_etoile",
        "None": "stmt_etoile -> stmt stmt_etoile",
        "EOF": "stmt_etoile -> ε",
        "END": "stmt_etoile -> ε"
    },
    
    "Def": {
        "def": "Def -> def IDENTIFIER ( arg ) : suite"
    },
    "arg": {
        "IDENTIFIER": "arg -> IDENTIFIER next_arg",
        ")": "arg -> ε"
    },
    "next_arg": {
        ",": "next_arg -> , IDENTIFIER next_arg",
        ")": "next_arg -> ε"
    },
    "suite": {
        "NEWLINE": "suite -> NEWLINE BEGIN stmt stmt_etoile END",
        "return": "suite -> simple_stmt NEWLINE",
        "print": "suite -> simple_stmt NEWLINE",
        "IDENTIFIER": "suite -> simple_stmt NEWLINE"
    },
    "simple_stmt": {
        "return": "simple_stmt -> return expr_init",
        "print": "simple_stmt -> print ( expr_init )",
        "IDENTIFIER": "simple_stmt -> IDENTIFIER simple_stmt_ident",
        "-": "simple_stmt -> expr_init",
        "not": "simple_stmt -> expr_init",
        "NUMBER": "simple_stmt -> expr_init",
        "string": "simple_stmt -> expr_init",
        "True": "simple_stmt -> expr_init",
        "False": "simple_stmt -> expr_init",
        "None": "simple_stmt -> expr_init"
    },
    "simple_stmt_ident": {
        "=": "simple_stmt_ident -> = expr_init",
        "(": "simple_stmt_ident -> expr_ident",
        "NEWLINE":"simple_stmt_ident -> expr_ident"
    },
    "stmt": {
        "return": "stmt -> simple_stmt NEWLINE",
        "print": "stmt -> simple_stmt NEWLINE",
        "IDENTIFIER": "stmt -> simple_stmt NEWLINE",
        "if": "stmt -> if expr_init : suite else",
        "for": "stmt -> for expr_init in expr_init : suite"
    },
    "else": {
        "Else": "else -> Else : suite",
        "NEWLINE": "else -> ε",
        "END": "else -> ε"
    },
    "expr_init": {
        "(": "expr_init -> expr expr_droite",
        "-": "expr_init -> expr expr_droite",
        "not": "expr_init -> expr expr_droite",
        "[": "expr_init -> expr expr_droite",
        "NUMBER": "expr_init -> expr expr_droite",
        "string": "expr_init -> expr expr_droite",
        "True": "expr_init -> expr expr_droite",
        "False": "expr_init -> expr expr_droite",
        "None": "expr_init -> expr expr_droite"
    },
    "expr": {
        "(": "expr -> ( expre )",
        "-": "expr -> - expre",
        "not": "expr -> not expre",
        "[": "expr -> [ expr_etoile ]",
        "NUMBER": "expr -> const",
        "string": "expr -> const",
        "True": "expr -> const",
        "False": "expr -> const",
        "None": "expr -> const"
    },
    
        "expr_identif": {
        "IDENTIFIER": "expr_identif -> IDENTIFIER expr_ident"
    },
    "expre": {
        "(": "expre -> expr",
        "-": "expre -> expr",
        "not": "expre -> expr",
        "[": "expre -> expr",
        "NUMBER": "expre -> expr",
        "string": "expre -> expr",
        "True": "expre -> expr",
        "False": "expre -> expr",
        "None": "expre -> expr",
        "IDENTIFIER": "expre -> expr_identif"
    },
    "expr_prime": {
        "[": "expr_prime -> [ expr ]",
        "+": "expr_prime -> OPERATOR_UNARY expr",
        "-": "expr_prime -> OPERATOR_UNARY expr",
        "*": "expr_prime -> OPERATOR_UNARY expr",
        "/": "expr_prime -> OPERATOR_UNARY expr",
        "%": "expr_prime -> OPERATOR_UNARY expr",
        "<": "expr_prime -> OPERATOR_UNARY expr",
        ">": "expr_prime -> OPERATOR_UNARY expr",
        "!=": "expr_prime -> OPERATOR_UNARY expr",
        "=": "expr_prime -> OPERATOR_UNARY expr"
    },
    "expr_ident": {
        "(": "expr_ident -> ( expr_etoile )",
        ")": "expr_ident -> ε",
        "]": "expr_ident -> ε",
        ",": "expr_ident -> ε",
        "+": "expr_ident -> ε",
        "-": "expr_ident -> ε",
        "*": "expr_ident -> ε",
        "/": "expr_ident -> ε",
        "%": "expr_ident -> ε",
        "<": "expr_ident -> ε",
        ">": "expr_ident -> ε",
        "!=": "expr_ident -> ε",
        "==": "expr_ident -> ε",
        "=": "expr_ident -> ε"
    },
    "expr_droite": {
        "]": "expr_droite -> ε",
        "NEWLINE": "expr_droite -> ε",
        ",": "expr_droite -> ε",
        "+": "expr_droite -> expr_prime expr_droite",
        "-": "expr_droite -> expr_prime expr_droite",
        "*": "expr_droite -> expr_prime expr_droite",
        "/": "expr_droite -> expr_prime expr_droite",
        "%": "expr_droite -> expr_prime expr_droite",
        "<": "expr_droite -> expr_prime expr_droite",
        ">": "expr_droite -> expr_prime expr_droite",
        "!=": "expr_droite -> expr_prime expr_droite",
        "=": "expr_droite -> expr_prime expr_droite"
    },
    "expr_etoile": {
        "]": "expr_etoile -> ε",
        "(": "expr_etoile -> expre expr_plus",
        "IDENTIFIER": "expr_etoile -> expre expr_plus",
        "NUMBER": "expr_etoile -> expre expr_plus",
        "string": "expr_etoile -> expre expr_plus",
        "True": "expr_etoile -> expre expr_plus",
        "False": "expr_etoile -> expre expr_plus",
        "None": "expr_etoile -> expre expr_plus"
    },
    "expr_plus": {
        "]": "expr_plus -> ε",
        ",": "expr_plus -> , expre expr_plus"
    },
    "OPERATOR_UNARY": {
        "+": "OPERATOR_UNARY -> +",
        "-": "OPERATOR_UNARY -> -",
        "*": "OPERATOR_UNARY -> *",
        "//": "OPERATOR_UNARY -> //",
        "%": "OPERATOR_UNARY -> %",
        "<": "OPERATOR_UNARY -> < double",
        ">": "OPERATOR_UNARY -> > double",
        "!=": "OPERATOR_UNARY -> ! =",
        "=": "OPERATOR_UNARY -> = double"
    },
    "double": {
        "=": "double -> =",
        ")": "double -> ε",
        "]": "double -> ε",
        ",": "double -> ε",
        "+": "double -> ε",
        "-": "double -> ε",
        "*": "double -> ε",
        "/": "double -> ε",
        "%": "double -> ε",
        "<": "double -> ε",
        ">": "double -> ε",
        "!=": "double -> ε"
    },
    "const": {
        "NUMBER": "const -> NUMBER",
        "string": "const -> string",
        "True": "const -> True",
        "False": "const -> False",
        "None": "const -> None"
    }

}


def parse_with_tokens(ll1_table, tokens, start_symbol):
    """
    Analyse syntaxique adaptée aux classes Token.
    
    Args:
        ll1_table (dict): La table LL(1), un dictionnaire avec non-terminaux et terminaux.
        tokens (list[BaseToken]): Liste des tokens à analyser.
        start_symbol (str): Le symbole de départ de la grammaire.
    
    Returns:
        bool: True si la chaîne est acceptée, False sinon.
    """
    # Ajouter un token spécial EOF pour marquer la fin de la chaîne
    #eof_token = BaseToken(TokenType.EOF, "$", -1, -1)
    #tokens.append(eof_token)
    
    # Initialiser la pile avec le symbole de départ et EOF
    stack = [start_symbol]
    
    # Pointeur sur le token courant
    index = 0
    
    while stack:
        top = stack[0]  # Extraire le sommet de la pile
        stack = stack[1:]
        current_token = tokens[index]  # Lire le token courant
        # Si le sommet est un terminal (valeur littérale)
        if top == current_token.analyse_syntaxique():
            #print(f"Match terminal: {top}")
            index += 1  # Avancer dans les tokens
        elif current_token.type.value == "EOF":
            # La pile contient $ et le token courant est également EOF
            if current_token.type == TokenType.EOF:
                print("Analyse terminée avec succès.")
                return True
            else:
                print("Erreur: Fin de chaîne attendue mais non trouvée.",current_token.type,top)
                return False
        elif top in ll1_table:
            # Trouver la production pour ce non-terminal et ce token courant
            token_type = current_token.analyse_syntaxique()
            if token_type in ll1_table[top]:
                production = ll1_table[top][token_type]
                print(f"Appliquer règle: {production}")
                # Ajouter les symboles de la règle dans la pile (dans l'ordre inverse)
                symbols = production.split("->")[1].strip().split()
                if symbols != ["ε"]:
                    #print("symbole:",symbols)# Ignorer ε (epsilon)
                    stack = symbols + stack
                    
            else:
                print(f"Erreur: Aucun règle pour {top} avec {token_type}.")
                return False
        else:
            print(f"Erreur: Symbole inattendu {top} {current_token.analyse_syntaxique()}.")
            return False
    
    # Si la pile est vide mais il reste des tokens, erreur
    if index < len(tokens) - 1:
        print(f"Erreur: Tokens restants non analysés {tokens[index:]}")
        return False
    
    print("Analyse réussie.")
    return True
