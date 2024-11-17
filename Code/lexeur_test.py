from typing import List, Tuple
from analyse_lexicale.fonction_lexicale import Lexeur

# Fonction pour tester les tokens générés par rapport aux attendus
def test_lexer(code: str, expected: List[Tuple[str, str, int, int]]):
    generated_tokens = Lexeur(code).Tokenisation()
    matched = 0
    missing_tokens = []
    extra_tokens = []

    # Comparaison des tokens
    for token in expected:
        if token in generated_tokens:
            matched += 1
        else:
            missing_tokens.append(token)

    for token in generated_tokens:
        if token not in expected:
            extra_tokens.append(token)

    total_expected = len(expected)
    accuracy = (matched / total_expected) * 100 if total_expected > 0 else 0

    # Rapport
    print(f"Taux de réussite : {accuracy:.2f}%")
    print(f"Tokens manquants : {missing_tokens}")
    print(f"Tokens en trop : {extra_tokens}")

# Exemple de code source
code_source = """
# Début du programme
def calcul_complexe(a, b):
    somme = a + b
    produit = a * b
    division = a / b
    reste = a % b
    quotient = a // b
    puissance = a ** b
    if a == b:
        print("Les nombres sont égaux")
    elif a != b:
        print("Les nombres sont différents")
    return somme, produit, quotient, puissance

def main():
    x = 10
    y = 5
    result = calcul_complexe(x, y)

if __name__ == "__main__":
    main()
"""

# Tokens attendus (simplifié pour l'exemple)
expected_tokens = [COMMENT(# Début du programme) at line 1, column 0,
NEWLINE() at line 1, column 21,
KEYWORD(def) at line 2, column 0,
IDENTIFIER(calcul_complexe) at line 2, column 4,
PUNCTUATION(() at line 2, column 18,
IDENTIFIER(a) at line 2, column 19,
PUNCTUATION(,) at line 2, column 20,
IDENTIFIER(b) at line 2, column 22,
PUNCTUATION()) at line 2, column 23,
PUNCTUATION(:) at line 2, column 24,
NEWLINE() at line 3, column 0,
COMMENT(# Opérations arithmétiques de base) at line 3, column 4,
NEWLINE() at line 4, column 0,
IDENTIFIER(somme) at line 4, column 4,
OPERATOR_UNARY(=) at line 4, column 10,
IDENTIFIER(a) at line 4, column 12,
OPERATOR_BINARY(+) at line 4, column 14,
IDENTIFIER(b) at line 4, column 16,
NEWLINE() at line 5, column 0,
IDENTIFIER(produit) at line 5, column 4,
OPERATOR_UNARY(=) at line 5, column 12,
IDENTIFIER(a) at line 5, column 14,
OPERATOR_BINARY(*) at line 5, column 16,
IDENTIFIER(b) at line 5, column 18,
NEWLINE() at line 6, column 0,
IDENTIFIER(division) at line 6, column 4,
OPERATOR_UNARY(=) at line 6, column 13,
IDENTIFIER(a) at line 6, column 15,
OPERATOR_BINARY(/) at line 6, column 17,
IDENTIFIER(b) at line 6, column 19,
NEWLINE() at line 7, column 0,
IDENTIFIER(reste) at line 7, column 4,
OPERATOR_UNARY(=) at line 7, column 10,
IDENTIFIER(a) at line 7, column 12,
OPERATOR_BINARY(%) at line 7, column 14,
IDENTIFIER(b) at line 7, column 16,
NEWLINE() at line 8, column 0,
IDENTIFIER(quotient) at line 8, column 4,
OPERATOR_UNARY(=) at line 8, column 13,
IDENTIFIER(a) at line 8, column 15,
OPERATOR_BINARY(//) at line 8, column 17,
IDENTIFIER(b) at line 8, column 19,
NEWLINE() at line 9, column 0,
IDENTIFIER(puissance) at line 9, column 4,
OPERATOR_UNARY(=) at line 9, column 14,
IDENTIFIER(a) at line 9, column 16,
OPERATOR_BINARY(**) at line 9, column 18,
IDENTIFIER(b) at line 9, column 20,
NEWLINE() at line 10, column 0,
COMMENT(# Opérations logiques et comparaisons) at line 10, column 4,
NEWLINE() at line 11, column 0,
KEYWORD(if) at line 11, column 4,
IDENTIFIER(a) at line 11, column 7,
OPERATOR_BINARY(==) at line 11, column 9,
IDENTIFIER(b) at line 11, column 12,
PUNCTUATION(:) at line 11, column 13,
NEWLINE() at line 12, column 0,
BEGIN() at line 12, column 4,
KEYWORD(print) at line 12, column 8,
PUNCTUATION(() at line 12, column 13,
STRING("Les nombres sont égaux") at line 12, column 14,
PUNCTUATION()) at line 12, column 38,
NEWLINE() at line 13, column 0,
END() at line 13, column 4,
KEYWORD(elif) at line 13, column 8,
IDENTIFIER(a) at line 13, column 13,
OPERATOR_BINARY(!=) at line 13, column 15,
IDENTIFIER(b) at line 13, column 18,
PUNCTUATION(:) at line 13, column 19,
NEWLINE() at line 14, column 0,
BEGIN() at line 14, column 4,
KEYWORD(print) at line 14, column 8,
PUNCTUATION(() at line 14, column 13,
STRING("Les nombres sont différents") at line 14, column 14,
PUNCTUATION()) at line 14, column 39,
NEWLINE() at line 15, column 0,
END() at line 15, column 4,
COMMENT(\# Comparaisons binaires) at line 16, column 4,
NEWLINE() at line 17, column 0,
KEYWORD(if) at line 17, column 4,
IDENTIFIER(a) at line 17, column 7,
OPERATOR_BINARY(>=) at line 17, column 9,
IDENTIFIER(b) at line 17, column 12,
]

# Exécuter le test
test_lexer(code_source, expected_tokens)
