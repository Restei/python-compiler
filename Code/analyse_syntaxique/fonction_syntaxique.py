from analyse_lexicale.token import *
from analyse_syntaxique.arbre import *



tableau_des_symboles_directeur_ll1_ultime = {
    "file": {#ok1
        "NEWLINE": "file -> NEWLINE def_etoile stmt stmt_etoile EOF",
        "def": "file -> def_etoile stmt stmt_etoile EOF",
        "ident": "file -> def_etoile stmt stmt_etoile EOF",
        "return": "file -> def_etoile stmt stmt_etoile EOF",
        "print": "file -> def_etoile stmt stmt_etoile EOF",
        "if": "file -> def_etoile stmt stmt_etoile EOF",
        "for": "file -> def_etoile stmt stmt_etoile EOF",
    },
    "def_etoile": {#ok1
        "def": "def_etoile -> Def def_etoile",
        "ident": "def_etoile -> ε",
        "return": "def_etoile -> ε",
        "print": "def_etoile -> ε",
        "if": "def_etoile -> ε",
        "for": "def_etoile -> ε",
    },
    "stmt_etoile": {#ok1
        "EOF": "stmt_etoile -> ε",
        "END": "stmt_etoile -> ε",
        "ident": "stmt_etoile -> stmt stmt_etoile",
        "return": "stmt_etoile -> stmt stmt_etoile",
        "print": "stmt_etoile -> stmt stmt_etoile",
        "if": "stmt_etoile -> stmt stmt_etoile",
        "for": "stmt_etoile -> stmt stmt_etoile",
    },
    "Def": {#ok1
        "def": "Def -> def ident ( arg ) : suite",
    },
    "arg": {#ok1
        "ident": "arg -> ident next_arg",
        ")": "arg -> ε",
    },
    "next_arg": {#ok1
        ",": "next_arg -> , ident next_arg",
        ")": "next_arg -> ε",
    },
    "suite": {#ok1
        "NEWLINE": "suite -> NEWLINE BEGIN stmt stmt_etoile END",
        "ident": "suite -> simple_stmt NEWLINE",
        "return": "suite -> simple_stmt NEWLINE",
        "print": "suite -> simple_stmt NEWLINE",
    },
    "simple_stmt": { #ok1
        "ident": "simple_stmt -> ident simple_stmt_tail",
        "return": "simple_stmt -> return expr_init",
        "print": "simple_stmt -> print ( expr_init )",
    },
        
    "simple_stmt_tail":{ #ok1
        "(":"simple_stmt_tail -> ( argument )",
        "=":"simple_stmt_tail -> simple_stmt_tail_tail = expr_init",
        "[":"simple_stmt_tail -> simple_stmt_tail_tail = expr_init"
        },
    
    "simple_stmt_tail_tail":{ #ok1
        "=":"simple_stmt_tail_tail -> ε",
        "[":"simple_stmt_tail_tail -> [ expr_init ] simple_stmt_tail_tail"
        },

    "argument":{ #ok1
        "ident": "argument -> expr_init next_argument",
        "(": "argument -> expr_init next_argument",
        ")": "argument -> ε",
        "]": "argument -> ε",
        "-": "argument -> expr_init next_argument",
        "not": "argument -> expr_init next_argument",
        "integer": "argument -> expr_init next_argument",
        "string": "argument -> expr_init next_argument",
        "True": "argument -> expr_init next_argument",
        "False": "argument -> expr_init next_argument",
        "[": "argument -> expr_init next_argument",
        "None": "argument -> expr_init next_argument"
        },
    "next_argument": { #ok1
        ",": "next_argument -> , expr_init next_argument",
        ")": "next_argument -> ε",
        "]": "next_argument -> ε",
    },
    "stmt": { #ok1
        "ident": "stmt -> simple_stmt NEWLINE",
        "return": "stmt -> simple_stmt NEWLINE",
        "print": "stmt -> simple_stmt NEWLINE",
        "if": "stmt -> if expr_init : suite Else",
        "for": "stmt -> for expr_init in expr_init : suite",
    },
    
    "Else": { #ok1
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
    
    "expr_init": { #ok1
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
    "expr_logic": { #ok1
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
    "expr_logic_tail": { #ok1
        "or": "expr_logic_tail -> or expr_comp expr_logic_tail",
        "and": "expr_logic_tail -> and expr_comp expr_logic_tail",
        "NEWLINE": "expr_logic_tail -> ε",
        ":": "expr_logic_tail -> ε",
        "in": "expr_logic_tail -> ε",
        ",": "expr_logic_tail -> ε",
        "]": "expr_logic_tail -> ε",
        ")": "expr_logic_tail -> ε"
    },
    "expr_comp": { #ok1
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
    "expr_comp_tail": { #ok1
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
    "comp_op": { #ok1
        "<": "comp_op -> <",
        "<=": "comp_op -> <=",
        ">": "comp_op -> >",
        ">=": "comp_op -> >=",
        "==": "comp_op -> ==",
        "!=": "comp_op -> !="
    },
    "expr_low": { #ok1
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
    "expr_low_tail": { #ok1
        "+": "expr_low_tail -> + expr_high expr_low_tail",
        "-": "expr_low_tail -> - expr_high expr_low_tail",
        "NEWLINE": "expr_low_tail -> ε",
        "in": "expr_low_tail -> ε",
        ",": "expr_low_tail -> ε",
        "]": "expr_low_tail -> ε",
        "or": "expr_low_tail -> ε",
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
    "expr_high": { #ok1
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
    "expr_high_tail": { #ok1
        "*": "expr_high_tail -> * expr_unary expr_high_tail",
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
    "expr_unary": { #ok1
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
    "expr_primary": { #ok1
        "ident": "expr_primary -> expr_primary_extra",
        "(": "expr_primary -> ( expr_init )",
        "[": "expr_primary -> [ argument ]",
        "integer": "expr_primary -> const",
        "string": "expr_primary -> const",
        "True": "expr_primary -> const",
        "False": "expr_primary -> const",
        "None": "expr_primary -> const"
    },
    "expr_primary_extra": { #ok1
        "ident": "expr_primary_extra -> ident expr_primary_tail"
    },
    "expr_primary_tail": { #ok
        "*": "expr_primary_tail -> expr_primary_tail2",
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
        "(": "expr_primary_tail -> ( argument ) ",
        ")": "expr_primary_tail -> expr_primary_tail2"
    },
    
    "expr_primary_tail2": { #ok1
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
        "//": "expr_primary_tail2 -> ε",
        "%": "expr_primary_tail2 -> ε",
    },
    "const": { #ok1
        "integer": "const -> integer",
        "string": "const -> string",
        "True": "const -> True",
        "False": "const -> False",
        "None": "const -> None"
    }
}

# Nouvelle liste pour collecter les erreurs
errors = []


def synchroniser(tokens, index, points_synchronisation):
    """
    Avancer le pointeur des tokens jusqu'à atteindre un point de synchronisation.
    Cette fonction permet de sauter les tokens non valides après une erreur,
    afin de reprendre l'analyse à un point logique (par exemple, un NEWLINE ou EOF).

    Args:
        tokens (list[BaseToken]): Liste des tokens à analyser.
        index (int): Index actuel dans la liste des tokens.
        points_synchronisation (list[str]): Points où l'analyse peut reprendre.

    Returns:
        int: Nouvel index après synchronisation.
    """
    while index < len(tokens) and tokens[index].analyse_syntaxique() not in points_synchronisation:
        index += 1  # Avancer jusqu'à atteindre un point de synchronisation
    return index

def parse_with_tokens(ll1_table, tokens, start_symbol):
    """
    Analyse syntaxique adaptée aux classes Token, avec gestion des erreurs syntaxiques et lexicales.
    Le parseur suit une table LL(1) pour analyser les tokens et construire un AST.

    Args:
        ll1_table (dict): La table LL(1), un dictionnaire avec non-terminaux et terminaux.
        tokens (list[BaseToken]): Liste des tokens à analyser.
        start_symbol (str): Le symbole de départ de la grammaire.

    Returns:
        bool: True si la chaîne est acceptée, sinon False avec un résumé des erreurs.
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

    # Initialisation de l'AST avec un noeud racine
    file = Node("file")  # Noeud racine de l'AST
    current_node = file  # Noeud actuel utilisé pour ajouter les enfants
    save_token = tokens[0] if len(tokens)>0 else None
    while stack:
        # Extraire le sommet de la pile
        top = stack.pop(0)
        # Obtenir le token courant (ou None si on dépasse la liste)
        current_token = tokens[index] if index < len(tokens) else None


        if save_token.type == TokenType.END:
            if current_token.type != TokenType.END:
                while current_node.name not in ["suite","file"]:
                    current_node = current_node.father
        save_token = current_token
        # Vérifier si le token courant est valide
        if current_token is None or not hasattr(current_token, "analyse_syntaxique"):
            # Ajouter une erreur lexicale si le token est invalide ou manquant
            #errors.append(
            #    f"Erreur lexicale : Impossible de détecter le token à l'index {index}. "
            #    f"Token invalide ou non reconnu. {current_token.value}"
            #)
            break  # Arrêter l'analyse si un problème lexical est détecté

        # Vérification 1 : Correspondance entre le sommet de la pile et le token courant
        if top == current_token.analyse_syntaxique():
            #print(f"Correspondance trouvée : {top}")
            # Ajouter le token correspondant comme enfant de l'AST
            index += 1  # Passer au token suivant

        # Vérification 2 : Si le token courant est EOF
        elif current_token.type.value == "EOF":
            # La pile contient $ et le token courant est également EOF
            if current_token.type == TokenType.EOF:
                #file.dessine()

                #print("Analyse terminée avec succès.")
                # Afficher toutes les erreurs détectées
                top = stack.pop(0)
                index+=1
                continue
            else:
                # Sinon, signaler une erreur de fin inattendue
                errors.append(
                    f"Erreur : Fin de fichier atteinte mais la pile contient encore {stack}. "
                    f"Impossible de compléter l'analyse."
                )
                break

        elif current_token == TokenType.UNKNOWN:
            index+=1
            current_token = tokens[index] if index < len(tokens) else None
            continue

        # Vérification 3 : Si le sommet de la pile est un non-terminal
        elif top in ll1_table:
            # Obtenir le type du token courant pour rechercher une règle
            token_type = current_token.analyse_syntaxique()
            if token_type in ll1_table[top]:
                # Trouver la règle correspondante dans la table LL(1)
                production = ll1_table[top][token_type]
                #print(f"Utilisation de la règle: {production}")
                # Ajouter un noeud correspondant à la règle dans l'arbre syntaxique
                if token_type in ['integer','string']:
                    current_node = current_node.ajouter_fils_arbre(production,current_token.value)
                else:
                    current_node = current_node.ajouter_fils_arbre(production)
                # Ajouter les symboles de la règle dans la pile
                symbols = production.split("->")[1].strip().split()
                if symbols != ["ε"]:  # Ignorer epsilon (productions vides)
                    stack = symbols + stack  # Ajouter les symboles dans la pile

            else:
                # Aucune règle trouvée : ajouter une erreur syntaxique
                expected_tokens = list(ll1_table[top].keys())
                errors.append(
                    f"Erreur syntaxique : Aucun règle trouvée pour {top} avec le token {token_type}. "
                    f"Ligne {current_token.line}, colonne {current_token.column}. "
                    f"Attendu : {expected_tokens}, trouvé : {token_type}."
                )
                erreur = top + " -> erreur" 
                top = stack[0]
                current_node.ajouter_fils_arbre(erreur)

                # Récupération : Passer au prochain point de synchronisation
                if top in ll1_table:
                    index = synchroniser(tokens, index,ll1_table[top])
                    print(tokens[index])
                continue

        # Vérification 4 : Symbole inattendu au sommet de la pile
        else:
            errors.append(
                f"Erreur syntaxique : Symbole inattendu '{top}' au sommet de la pile. "
                f"Ligne {current_token.line}, colonne {current_token.column}"
            )
            # Récupération : Passer au prochain point de synchronisation
            index = synchroniser(tokens, index, ["NEWLINE", "EOF"])
            continue

    # Vérification finale : Des tokens restants non analysés
    if index < len(tokens):
        remaining_tokens = tokens[index:]
        errors.append(
            f"Erreur : Tokens non analysés restants : "
            f"{[token.analyse_syntaxique() for token in remaining_tokens]}"
        )
    if errors:
        print(f"Analyse terminée avec des erreurs:")
        for error in errors:
            print(error)
    # Si aucune erreur n'a été rencontrée, l'analyse est réussie
    else:
        print("Analyse réussie.")
        file.replace_identifier(ident_list)
        file.AST()  
    return errors