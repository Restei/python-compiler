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