tableau_des_symboles_directeur ={
    "file": {
        "NEWLINE": "file -> NEWLINE def_etoile stmt stmt_etoile EOF",
        "Def": "file -> def_etoile stmt stmt_etoile EOF",
        "ident": "file -> def_etoile stmt stmt_etoile EOF",
        "return": "file -> def_etoile stmt stmt_etoile EOF",
        "print": "file -> def_etoile stmt stmt_etoile EOF",
        "if": "file -> def_etoile stmt stmt_etoile EOF",
        "for": "file -> def_etoile stmt stmt_etoile EOF",
        "-": "file -> def_etoile stmt stmt_etoile EOF",
        "not": "file -> def_etoile stmt stmt_etoile EOF",
        "integer": "file -> def_etoile stmt stmt_etoile EOF",
        "string": "file -> def_etoile stmt stmt_etoile EOF",
        "True": "file -> def_etoile stmt stmt_etoile EOF",
        "False": "file -> def_etoile stmt stmt_etoile EOF",
        "None": "file -> def_etoile stmt stmt_etoile EOF"
    },
    "def_etoile": {
        "Def": "def_etoile -> def def_etoile",
        "ident": "def_etoile -> ε",
        "return": "def_etoile -> ε",
        "print": "def_etoile -> ε",
        "if": "def_etoile -> ε",
        "for": "def_etoile -> ε",
        "-": "def_etoile -> ε",
        "not": "def_etoile -> ε",
        "integer": "def_etoile -> ε",
        "string": "def_etoile -> ε",
        "True": "def_etoile -> ε",
        "False": "def_etoile -> ε",
        "None": "def_etoile -> ε"
    },
    "stmt_etoile": {
        "ident": "stmt_etoile -> stmt stmt_etoile",
        "return": "stmt_etoile -> stmt stmt_etoile",
        "print": "stmt_etoile -> stmt stmt_etoile",
        "if": "stmt_etoile -> stmt stmt_etoile",
        "for": "stmt_etoile -> stmt stmt_etoile",
        "-": "stmt_etoile -> stmt stmt_etoile",
        "not": "stmt_etoile -> stmt stmt_etoile",
        "integer": "stmt_etoile -> stmt stmt_etoile",
        "string": "stmt_etoile -> stmt stmt_etoile",
        "True": "stmt_etoile -> stmt stmt_etoile",
        "False": "stmt_etoile -> stmt stmt_etoile",
        "None": "stmt_etoile -> stmt stmt_etoile",
        "EOF": "stmt_etoile -> ε",
        "END": "stmt_etoile -> ε"
    },
    
    "def": {
        "Def": "def -> Def ident ( arg ) : suite"
    },
    "arg": {
        "ident": "arg -> ident next_arg",
        ")": "arg -> ε"
    },
    "next_arg": {
        ",": "next_arg -> , ident next_arg",
        ")": "next_arg -> ε"
    },
    "suite": {
        "NEWLINE": "suite -> NEWLINE BEGIN stmt stmt_etoile END",
        "return": "suite -> simple_stmt NEWLINE",
        "print": "suite -> simple_stmt NEWLINE",
        "ident": "suite -> simple_stmt NEWLINE"
    },
    "simple_stmt": {
        "return": "simple_stmt -> return expr_init",
        "print": "simple_stmt -> print ( expr_init )",
        "ident": "simple_stmt -> ident simple_stmt_ident",
        "-": "simple_stmt -> expr_init",
        "not": "simple_stmt -> expr_init",
        "integer": "simple_stmt -> expr_init",
        "string": "simple_stmt -> expr_init",
        "True": "simple_stmt -> expr_init",
        "False": "simple_stmt -> expr_init",
        "None": "simple_stmt -> expr_init"
    },
    "simple_stmt_ident": {
        "=": "simple_stmt_ident -> = expr_init",
        "(": "simple_stmt_ident -> expr_ident"
    },
    "stmt": {
        "return": "stmt -> simple_stmt NEWLINE",
        "print": "stmt -> simple_stmt NEWLINE",
        "ident": "stmt -> simple_stmt NEWLINE",
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
        "integer": "expr_init -> expr expr_droite",
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
        "integer": "expr -> const",
        "string": "expr -> const",
        "True": "expr -> const",
        "False": "expr -> const",
        "None": "expr -> const"
    },
    
        "expr_identif": {
        "ident": "expr_identif -> ident expr_ident"
    },
    "expre": {
        "(": "expre -> expr",
        "-": "expre -> expr",
        "not": "expre -> expr",
        "[": "expre -> expr",
        "integer": "expre -> expr",
        "string": "expre -> expr",
        "True": "expre -> expr",
        "False": "expre -> expr",
        "None": "expre -> expr",
        "ident": "expre -> expr_identif"
    },
    "expr_prime": {
        "[": "expr_prime -> [ expr ]",
        "+": "expr_prime -> binop expr",
        "-": "expr_prime -> binop expr",
        "*": "expr_prime -> binop expr",
        "/": "expr_prime -> binop expr",
        "%": "expr_prime -> binop expr",
        "<": "expr_prime -> binop expr",
        ">": "expr_prime -> binop expr",
        "!=": "expr_prime -> binop expr",
        "=": "expr_prime -> binop expr"
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
        "=": "expr_ident -> ε"
    },
    "expr_droite": {
        "]": "expr_droite -> ε",
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
        "ident": "expr_etoile -> expre expr_plus",
        "integer": "expr_etoile -> expre expr_plus",
        "string": "expr_etoile -> expre expr_plus",
        "True": "expr_etoile -> expre expr_plus",
        "False": "expr_etoile -> expre expr_plus",
        "None": "expr_etoile -> expre expr_plus"
    },
    "expr_plus": {
        "]": "expr_plus -> ε",
        ",": "expr_plus -> , expre expr_plus"
    },
    "binop": {
        "+": "binop -> +",
        "-": "binop -> -",
        "*": "binop -> *",
        "//": "binop -> //",
        "%": "binop -> %",
        "<": "binop -> < double",
        ">": "binop -> > double",
        "!=": "binop -> ! =",
        "=": "binop -> = double"
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
        "integer": "const -> integer",
        "string": "const -> string",
        "True": "const -> True",
        "False": "const -> False",
        "None": "const -> None"
    }

}

print(tableau_des_symboles_directeur["const"]["integer"])

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
        "ident":"simple_stmt_tail -> ( argument )",
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
        "-": "argument -> expr_init next_argument",
        "integer": "argument -> expr_init next_argument",
        "string": "argument -> expr_init next_argument",
        "True": "argument -> expr_init next_argument",
        "False": "argument -> expr_init next_argument",
        "None": "argument -> expr_init next_argument"
        },
    "next_argument": { #ok
        ",": "next_argument -> , expr_init next_argument",
        ")": "next_argument -> ε",
    },
    "stmt": { #ok
        "ident": "stmt -> simple_stmt NEWLINE",
        "return": "stmt -> simple_stmt NEWLINE",
        "print": "stmt -> simple_stmt NEWLINE",
        "if": "stmt -> if expr_init : suite else",
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
        "or": "expr_low_tail -> ε",
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
        "integer": "expr_unary -> expr_primary",
        "string": "expr_unary -> expr_primary",
        "True": "expr_unary -> expr_primary",
        "False": "expr_unary -> expr_primary",
        "None": "expr_unary -> expr_primary"
    },
    "expr_primary": { #ok
        "ident": "expr_primary -> expr_primary_extra",
        "(": "expr_primary -> ( argument )",
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
