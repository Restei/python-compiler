from analyse_lexicale.token import *
from analyse_syntaxique.arbre import *



tableau_des_symboles_directeur_ll1_ultime = {
    "file": {#ok
        "NEWLINE": "file -> NEWLINE def_etoile stmt stmt_etoile EOF",
        "def": "file -> def_etoile stmt stmt_etoile EOF",
        "ident": "file -> def_etoile stmt stmt_etoile EOF",
        "return": "file -> def_etoile stmt stmt_etoile EOF",
        "print": "file -> def_etoile stmt stmt_etoile EOF",
        "if": "file -> def_etoile stmt stmt_etoile EOF",
        "for": "file -> def_etoile stmt stmt_etoile EOF",
    },
    "def_etoile": {
        "def": "def_etoile -> Def def_etoile",
        "ident": "def_etoile -> ε",
        "return": "def_etoile -> ε",
        "print": "def_etoile -> ε",
        "if": "def_etoile -> ε",
        "for": "def_etoile -> ε",
    },
    "stmt_etoile": {#ok
        "EOF": "stmt_etoile -> ε",
        "END": "stmt_etoile -> ε",
        "ident": "stmt_etoile -> stmt stmt_etoile",
        "return": "stmt_etoile -> stmt stmt_etoile",
        "print": "stmt_etoile -> stmt stmt_etoile",
        "if": "stmt_etoile -> stmt stmt_etoile",
        "for": "stmt_etoile -> stmt stmt_etoile",
    },
    "Def": {#ok
        "def": "Def -> def ident ( arg ) : suite",
    },
    "arg": {#ok
        "ident": "arg -> ident next_arg",
        ")": "arg -> ε",
    },
    "next_arg": {#ok
        ",": "next_arg -> , ident next_arg",
        ")": "next_arg -> ε",
    },
    "suite": {#ok
        "NEWLINE": "suite -> NEWLINE BEGIN stmt stmt_etoile END",
        "ident": "suite -> simple_stmt NEWLINE",
        "return": "suite -> simple_stmt NEWLINE",
        "print": "suite -> simple_stmt NEWLINE",
    },
    "simple_stmt": { #ok
        "ident": "simple_stmt -> ident simple_stmt_tail",
        "return": "simple_stmt -> return expr_init",
        "print": "simple_stmt -> print ( expr_init )",
    },
        
    "simple_stmt_tail":{ #ok
        "(":"simple_stmt_tail -> ( argument )",
        "=":"simple_stmt_tail -> simple_stmt_tail_tail = expr_init",
        "[":"simple_stmt_tail -> simple_stmt_tail_tail = expr_init"
        },
    
    "simple_stmt_tail_tail":{ #ok
        "=":"simple_stmt_tail_tail -> ε",
        "[":"simple_stmt_tail_tail -> [ expr_init ] simple_stmt_tail_tail"
        },

    "argument":{ #ok
        "ident": "argument -> expr_init next_argument",
        "(": "argument -> expr_init next_argument",
        ")": "argument -> ε",
        "]": "argument -> ε",
        "-": "argument -> expr_init next_argument",
        "integer": "argument -> expr_init next_argument",
        "string": "argument -> expr_init next_argument",
        "True": "argument -> expr_init next_argument",
        "False": "argument -> expr_init next_argument",
        "False": "argument -> expr_init next_argument",
        "[": "argument -> expr_init next_argument",
        "None": "argument -> expr_init next_argument"
        },
    "next_argument": { #ok
        ",": "next_argument -> , expr_init next_argument",
        ")": "next_argument -> ε",
        "]": "next_argument -> ε",
    },
    "stmt": { #ok
        "ident": "stmt -> simple_stmt NEWLINE",
        "return": "stmt -> simple_stmt NEWLINE",
        "print": "stmt -> simple_stmt NEWLINE",
        "if": "stmt -> if expr_init : suite Else",
        "for": "stmt -> for expr_init in expr_init : suite",
    },
    
    "Else": { #ok
        "else": "Else -> else : suite",
        "NEWLINE": "Else -> ε",
        "EOF": "Else -> ε",
        "END": "Else -> ε",
        "ident": "Else -> ε",
        "return": "Else -> ε",
        "print": "Else -> ε",
        "if": "Else -> ε",
        "for": "Else -> ε",
    },
    
    "expr_init": { #ok
        "ident": "expr_init -> expr_logic",
        "(": "expr_init -> expr_logic",
        "[": "expr_init -> expr_logic",
        "-": "expr_init -> expr_logic",
        "not": "expr_init -> expr_logic",
        "integer": "expr_init -> expr_logic",
        "string": "expr_init -> expr_logic",
        "True": "expr_init -> expr_logic",
        "False": "expr_init -> expr_logic",
        "None": "expr_init -> expr_logic"
    },
    "expr_logic": { #ok
        "ident": "expr_logic -> expr_comp expr_logic_tail",
        "(": "expr_logic -> expr_comp expr_logic_tail",
        "[": "expr_logic -> expr_comp expr_logic_tail",
        "-": "expr_logic -> expr_comp expr_logic_tail",
        "not": "expr_logic -> expr_comp expr_logic_tail",
        "integer": "expr_logic -> expr_comp expr_logic_tail",
        "string": "expr_logic -> expr_comp expr_logic_tail",
        "True": "expr_logic -> expr_comp expr_logic_tail",
        "False": "expr_logic -> expr_comp expr_logic_tail",
        "None": "expr_logic -> expr_comp expr_logic_tail"
    },
    "expr_logic_tail": { #ok
        "or": "expr_logic_tail -> or expr_comp expr_logic_tail",
        "and": "expr_logic_tail -> and expr_comp expr_logic_tail",
        "NEWLINE": "expr_logic_tail -> ε",
        ":": "expr_logic_tail -> ε",
        "in": "expr_logic_tail -> ε",
        ",": "expr_logic_tail -> ε",
        "]": "expr_logic_tail -> ε",
        ")": "expr_logic_tail -> ε"
    },
    "expr_comp": { #ok
        "ident": "expr_comp -> expr_low expr_comp_tail",
        "(": "expr_comp -> expr_low expr_comp_tail",
        "[": "expr_comp -> expr_low expr_comp_tail",
        "-": "expr_comp -> expr_low expr_comp_tail",
        "not": "expr_comp -> expr_low expr_comp_tail",
        "integer": "expr_comp -> expr_low expr_comp_tail",
        "string": "expr_comp -> expr_low expr_comp_tail",
        "True": "expr_comp -> expr_low expr_comp_tail",
        "False": "expr_comp -> expr_low expr_comp_tail",
        "None": "expr_comp -> expr_low expr_comp_tail"
    },
    "expr_comp_tail": { #ok
        "<": "expr_comp_tail -> comp_op expr_low",
        "<=": "expr_comp_tail -> comp_op expr_low",
        ">": "expr_comp_tail -> comp_op expr_low",
        ">=": "expr_comp_tail -> comp_op expr_low",
        "==": "expr_comp_tail -> comp_op expr_low",
        "!=": "expr_comp_tail -> comp_op expr_low",
        "or": "expr_comp_tail -> ε",
        "and": "expr_comp_tail -> ε",
        "NEWLINE": "expr_comp_tail -> ε",
        ":": "expr_comp_tail -> ε",
        "in": "expr_comp_tail -> ε",
        ",": "expr_comp_tail -> ε",
        "]": "expr_comp_tail -> ε",
        ")": "expr_comp_tail -> ε"
    },
    "comp_op": { #ok
        "<": "comp_op -> <",
        "<=": "comp_op -> <=",
        ">": "comp_op -> >",
        ">=": "comp_op -> >=",
        "==": "comp_op -> ==",
        "!=": "comp_op -> !="
    },
    "expr_low": { #ok
        "ident": "expr_low -> expr_high expr_low_tail",
        "(": "expr_low -> expr_high expr_low_tail",
        "[": "expr_low -> expr_high expr_low_tail",
        "-": "expr_low -> expr_high expr_low_tail",
        "not": "expr_low -> expr_high expr_low_tail",
        "integer": "expr_low -> expr_high expr_low_tail",
        "string": "expr_low -> expr_high expr_low_tail",
        "True": "expr_low -> expr_high expr_low_tail",
        "False": "expr_low -> expr_high expr_low_tail",
        "None": "expr_low -> expr_high expr_low_tail"
    },
    "expr_low_tail": { #ok
        "+": "expr_low_tail -> + expr_high expr_low_tail",
        "-": "expr_low_tail -> - expr_high expr_low_tail",
        "or": "expr_low_tail -> ε",
        "NEWLINE": "expr_low_tail -> ε",
        "in": "expr_low_tail -> ε",
        ",": "expr_low_tail -> ε",
        "]": "expr_low_tail -> ε",
        "and": "expr_low_tail -> ε",
        ":": "expr_low_tail -> ε",
        "<": "expr_low_tail -> ε",
        "<=": "expr_low_tail -> ε",
        ">": "expr_low_tail -> ε",
        ">=": "expr_low_tail -> ε",
        "==": "expr_low_tail -> ε",
        "!=": "expr_low_tail -> ε",
        ")": "expr_low_tail -> ε"
    },
    "expr_high": { #ok
        "ident": "expr_high -> expr_unary expr_high_tail",
        "(": "expr_high -> expr_unary expr_high_tail",
        "[": "expr_high -> expr_unary expr_high_tail",
        "-": "expr_high -> expr_unary expr_high_tail",
        "not": "expr_high -> expr_unary expr_high_tail",
        "integer": "expr_high -> expr_unary expr_high_tail",
        "string": "expr_high -> expr_unary expr_high_tail",
        "True": "expr_high -> expr_unary expr_high_tail",
        "False": "expr_high -> expr_unary expr_high_tail",
        "None": "expr_high -> expr_unary expr_high_tail"
    },
    "expr_high_tail": { #ok
        "*": "expr_high_tail -> * expr_unary expr_high_tail",
        "/": "expr_high_tail -> / expr_unary expr_high_tail",
        "//": "expr_high_tail -> // expr_unary expr_high_tail",
        "%": "expr_high_tail -> % expr_unary expr_high_tail",
        "+": "expr_high_tail -> ε",
        "-": "expr_high_tail -> ε",
        "or": "expr_high_tail -> ε",
        "and": "expr_high_tail -> ε",
        "NEWLINE": "expr_high_tail -> ε",
        ":": "expr_high_tail -> ε",
        "in": "expr_high_tail -> ε",
        ",": "expr_high_tail -> ε",
        "]": "expr_high_tail -> ε",
        "<": "expr_high_tail -> ε",
        "<=": "expr_high_tail -> ε",
        ">": "expr_high_tail -> ε",
        ">=": "expr_high_tail -> ε",
        "==": "expr_high_tail -> ε",
        "!=": "expr_high_tail -> ε",
        ")": "expr_high_tail -> ε"
    },
    "expr_unary": { #ok
        "-": "expr_unary -> - expr_primary",
        "not": "expr_unary -> not expr_primary",
        "ident": "expr_unary -> expr_primary",
        "(": "expr_unary -> expr_primary",
        "[": "expr_unary -> expr_primary",
        "integer": "expr_unary -> expr_primary",
        "string": "expr_unary -> expr_primary",
        "True": "expr_unary -> expr_primary",
        "False": "expr_unary -> expr_primary",
        "None": "expr_unary -> expr_primary"
    },
    "expr_primary": { #ok
        "ident": "expr_primary -> expr_primary_extra",
        "(": "expr_primary -> ( argument )",
        "[": "expr_primary -> [ argument ]",
        "integer": "expr_primary -> const",
        "string": "expr_primary -> const",
        "True": "expr_primary -> const",
        "False": "expr_primary -> const",
        "None": "expr_primary -> const"
    },
    "expr_primary_extra": { #ok
        "ident": "expr_primary_extra -> ident expr_primary_tail"
    },
    "expr_primary_tail": { #ok
        "*": "expr_primary_tail -> expr_primary_tail2",
        "/": "expr_primary_tail -> expr_primary_tail2",
        "//": "expr_primary_tail -> expr_primary_tail2",
        "%": "expr_primary_tail -> expr_primary_tail2",
        "+": "expr_primary_tail -> expr_primary_tail2",
        "-": "expr_primary_tail -> expr_primary_tail2",
        "or": "expr_primary_tail -> expr_primary_tail2",
        "and": "expr_primary_tail -> expr_primary_tail2",
        "NEWLINE": "expr_primary_tail -> expr_primary_tail2",
        ":": "expr_primary_tail -> expr_primary_tail2",
        "in": "expr_primary_tail -> expr_primary_tail2",
        ",": "expr_primary_tail -> expr_primary_tail2",
        "]": "expr_primary_tail -> expr_primary_tail2",
        "[": "expr_primary_tail -> expr_primary_tail2",
        "<": "expr_primary_tail -> expr_primary_tail2",
        "<=": "expr_primary_tail -> expr_primary_tail2",
        ">": "expr_primary_tail -> expr_primary_tail2",
        ">=": "expr_primary_tail -> expr_primary_tail2",
        "==": "expr_primary_tail -> expr_primary_tail2",
        "!=": "expr_primary_tail -> expr_primary_tail2",
        "(": "expr_primary_tail -> ( expr_init ) ",
        ")": "expr_primary_tail -> expr_primary_tail2"
    },
    
    "expr_primary_tail2": { #ok
        "NEWLINE": "expr_primary_tail2 -> ε",
        ")": "expr_primary_tail2 -> ε",
        ":": "expr_primary_tail2 -> ε",
        ",": "expr_primary_tail2 -> ε",
        "[": "expr_primary_tail2 -> [ expr_init ] expr_primary_tail ",
        "]": "expr_primary_tail2 -> ε",
        "in": "expr_primary_tail2 -> ε",
        "or": "expr_primary_tail2 -> ε",      
        "and": "expr_primary_tail2 -> ε", 
        "<": "expr_primary_tail2 -> ε",
        "<=": "expr_primary_tail2 -> ε",
        ">": "expr_primary_tail2 -> ε",
        ">=": "expr_primary_tail2 -> ε",
        "==": "expr_primary_tail2 -> ε",
        "!=": "expr_primary_tail2 -> ε",        
        "+": "expr_primary_tail2 -> ε",
        "-": "expr_primary_tail2 -> ε",  
        "*": "expr_primary_tail2 -> ε",
        "/": "expr_primary_tail2 -> ε",
        "//": "expr_primary_tail2 -> ε",
        "%": "expr_primary_tail2 -> ε",
    },
    "const": { #ok
        "integer": "const -> integer",
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
    ident_list =[]
    for elem in tokens:
        if elem.type == TokenType.IDENTIFIER:
            ident_list.append(elem.value)
    # Pointeur sur le token courant
    index = 0
    file = Node("file")
    node = file
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
                #file.dessine()
                file.replace_identifier(ident_list)
                file.AST()
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
                if token_type in ['ident','integer','string']:
                    node =node.ajouter_fils_arbre(production,current_token.value)
                else:
                    node =node.ajouter_fils_arbre(production)
                # Ajouter les symboles de la règle dans la pile (dans l'ordre inverse)
                symbols = production.split("->")[1].strip().split()
                if symbols != ["ε"]:
                    #print("symbole:",symbols)# Ignorer ε (epsilon)
                    stack = symbols + stack

            else:
                print(f"Erreur: Aucun règle pour {top} avec {token_type}.")
                print(f"{current_token}")
                return False
        else:
            print(f"Erreur: Symbole inattendu '{top}' trouvé à la position ligne {current_token.line}, colonne {current_token.column}.")

            
            return False
    
    # Si la pile est vide mais il reste des tokens, erreur
    if index < len(tokens) - 1:
        print(f"Erreur: Tokens restants non analysés {tokens[index:]}")
        return False
    
    print("Analyse réussie.")
    return True



