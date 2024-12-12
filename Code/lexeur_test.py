from typing import List, Tuple
from analyse_lexicale.fonction_lexicale import Lexeur

# Fonction pour tester les tokens générés par rapport aux attendus
def test_lexer(code: str, expected: List[Tuple[str, str, int, int]]):
    generated_token,errors = Lexeur(code).Tokenisation()
    matched = 0
    missing_tokens = []
    extra_tokens = []
    generated_tokens = []
    
    #for i in range(len(generated_token)):
    #    token = generated_token[i]
    for token in generated_token:
        generated_tokens.append((token.type.value,token.value,token.line,token.column))
        
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
code_source = """# Début du programme
def calcul_complexe(a, b):
    # Opérations arithmétiques de base
    somme = a + b  # Addition
    produit = a * b  # Multiplication
    division = a / b  # Division classique
    reste = a % b  # Modulo (reste de la division euclidienne)
    quotient = a // b  # Division entière
    puissance = a ** b  # Exponentiation

    # Opérations logiques et comparaisons
    if a == b:
        print("Les nombres sont égaux")
    elif a != b:
        print("Les nombres sont différents")

    # Comparaisons binaires
    if a >= b and a <= 100:
        print("a est entre b et 100")
    if a > 0 or b < 0:
        print("Un des nombres est positif")

    # Incrémentations et décrémentations
    a += 1  # Incrémentation de a
    b -= 1  # Décrémentation de b

    # Décalage binaire
    a_gauche = a << 2  # Décalage à gauche
    b_droite = b >> 3  # Décalage à droite

    return somme, produit, quotient, puissance, a_gauche, b_droite

# Fonction principale
def main():
    x = 10
    y = 5

    # Appel de la fonction avec des expressions complexes
    result = calcul_complexe(x, y)

# Appel de la fonction principale
if __name__ == "__main__":
    main()
"""

# Tokens attendus (simplifié pour l'exemple)
expected_tokens = [('NEWLINE', '', 2, 20), ('KEYWORD', 'def', 2, 24), ('IDENTIFIER', 'calcul_complexe', 2, 40), ('PUNCTUATION', '(', 2, 40),
                   ('IDENTIFIER', 'a', 2, 42), ('PUNCTUATION', ',', 2, 42), ('IDENTIFIER', 'b', 2, 45), ('PUNCTUATION', ')', 2, 45),
                   ('PUNCTUATION', ':', 2, 46), ('NEWLINE', '', 3, 47), ('INDENT', '', 3, 51), ('IDENTIFIER', 'somme', 4, 96), 
                   ('OPERATOR_UNARY', '=', 4, 97), ('IDENTIFIER', 'a', 4, 100), ('OPERATOR_UNARY', '+', 4, 101), ('IDENTIFIER', 'b', 4, 104), ('NEWLINE', '', 5, 116),
                   ('IDENTIFIER', 'produit', 5, 128), ('OPERATOR_UNARY', '=', 5, 129), ('IDENTIFIER', 'a', 5, 132), ('OPERATOR_UNARY', '*', 5, 133), 
                   ('IDENTIFIER', 'b', 5, 136), ('NEWLINE', '', 6, 154), ('IDENTIFIER', 'division', 6, 167), ('OPERATOR_UNARY', '=', 6, 168), ('IDENTIFIER', 'a', 6, 171), 
                   ('OPERATOR_UNARY', '/', 6, 172), ('IDENTIFIER', 'b', 6, 175), ('NEWLINE', '', 7, 197), ('IDENTIFIER', 'reste', 7, 207), ('OPERATOR_UNARY', '=', 7, 208), 
                   ('IDENTIFIER', 'a', 7, 211), ('OPERATOR_UNARY', '%', 7, 212), ('IDENTIFIER', 'b', 7, 215), ('NEWLINE', '', 8, 260), ('IDENTIFIER', 'quotient', 8, 273), 
                   ('OPERATOR_UNARY', '=', 8, 274), ('IDENTIFIER', 'a', 8, 277), ('OPERATOR_BINARY', '//', 8, 279), ('IDENTIFIER', 'b', 8, 282), ('NEWLINE', '', 9, 302), 
                   ('IDENTIFIER', 'puissance', 9, 316), ('OPERATOR_UNARY', '=', 9, 317), ('IDENTIFIER', 'a', 9, 320), ('OPERATOR_BINARY', '**', 9, 322), 
                   ('IDENTIFIER', 'b', 9, 325), ('NEWLINE', '', 10, 343),  ('KEYWORD', 'if', 12, 393), 
                   ('IDENTIFIER', 'a', 12, 395), ('OPERATOR_BINARY', '==', 12, 397), ('IDENTIFIER', 'b', 12, 400), ('PUNCTUATION', ':', 12, 400), ('NEWLINE', '', 13, 401), 
                   ('INDENT', '', 13, 409), ('KEYWORD', 'print', 13, 415), ('PUNCTUATION', '(', 13, 415), ('STRING', '"Les nombres sont égaux"', 13, 439), 
                   ('PUNCTUATION', ')', 13, 440), ('NEWLINE', '', 14, 441), ('DEDENT', '', 14, 445), ('KEYWORD', 'elif', 14, 450), ('IDENTIFIER', 'a', 14, 452), 
                   ('OPERATOR_BINARY', '!=', 14, 454), ('IDENTIFIER', 'b', 14, 457), ('PUNCTUATION', ':', 14, 457), ('NEWLINE', '', 15, 458), ('INDENT', '', 15, 466),
                   ('KEYWORD', 'print', 15, 472), ('PUNCTUATION', '(', 15, 472), ('STRING', '"Les nombres sont différents"', 15, 501), ('PUNCTUATION', ')', 15, 502), 
                   ('NEWLINE', '', 16, 503), ('DEDENT', '', 17, 508), ('KEYWORD', 'if', 18, 539), 
                   ('IDENTIFIER', 'a', 18, 541), ('OPERATOR_BINARY', '>=', 18, 543), ('IDENTIFIER', 'b', 18, 546), ('KEYWORD', 'and', 18, 550), ('IDENTIFIER', 'a', 18, 552), 
                   ('OPERATOR_BINARY', '<=', 18, 554), ('NUMBER', '100', 18, 559), ('PUNCTUATION', ':', 18, 559), ('NEWLINE', '', 19, 560), ('INDENT', '', 19, 568),
                   ('KEYWORD', 'print', 19, 574), ('PUNCTUATION', '(', 19, 574), ('STRING', '"a est entre b et 100"', 19, 596), ('PUNCTUATION', ')', 19, 597),
                   ('NEWLINE', '', 20, 598), ('DEDENT', '', 20, 602), ('KEYWORD', 'if', 20, 605), ('IDENTIFIER', 'a', 20, 607), ('OPERATOR_UNARY', '>', 20, 608),
                   ('NUMBER', '0', 20, 611), ('KEYWORD', 'or', 20, 614), ('IDENTIFIER', 'b', 20, 616), ('OPERATOR_UNARY', '<', 20, 617), ('NUMBER', '0', 20, 620), 
                   ('PUNCTUATION', ':', 20, 620), ('NEWLINE', '', 21, 621), ('INDENT', '', 21, 629), ('KEYWORD', 'print', 21, 635), ('PUNCTUATION', '(', 21, 635), 
                   ('STRING', '"Un des nombres est positif"', 21, 663), ('PUNCTUATION', ')', 21, 664), ('NEWLINE', '', 22, 665),
                   ('DEDENT', '', 23, 670),  ('IDENTIFIER', 'a', 24, 713), ('OPERATOR_BINARY', '+=', 24, 715), ('NUMBER', '1', 24, 718), 
                   ('NEWLINE', '', 25, 741), ('IDENTIFIER', 'b', 25, 747), ('OPERATOR_BINARY', '-=', 25, 749), ('NUMBER', '1', 25, 752), ('NEWLINE', '', 26, 775), 
                   ('IDENTIFIER', 'a_gauche', 28, 812), ('OPERATOR_UNARY', '=', 28, 813), ('IDENTIFIER', 'a', 28, 816), 
                   ('OPERATOR_BINARY', '<<', 28, 818), ('NUMBER', '2', 28, 821), ('NEWLINE', '', 29, 842), ('IDENTIFIER', 'b_droite', 29, 855), ('OPERATOR_UNARY', '=', 29, 856),
                   ('IDENTIFIER', 'b', 29, 859), ('OPERATOR_BINARY', '>>', 29, 861), ('NUMBER', '3', 29, 864), ('NEWLINE', '', 30, 885),
                   ('KEYWORD', 'return', 31, 897), ('IDENTIFIER', 'somme', 31, 903), ('PUNCTUATION', ',', 31, 903), ('IDENTIFIER', 'produit', 31, 912), 
                   ('PUNCTUATION', ',', 31, 912), ('IDENTIFIER', 'quotient', 31, 922), ('PUNCTUATION', ',', 31, 922), ('IDENTIFIER', 'puissance', 31, 933),
                   ('PUNCTUATION', ',', 31, 933), ('IDENTIFIER', 'a_gauche', 31, 943), ('PUNCTUATION', ',', 31, 943), ('IDENTIFIER', 'b_droite', 32, 953),
                   ('NEWLINE', '', 32, 953), ('DEDENT', '', 33, 954),('KEYWORD', 'def', 34, 980), 
                   ('IDENTIFIER', 'main', 34, 985), ('PUNCTUATION', '(', 34, 985), ('PUNCTUATION', ')', 34, 986), ('PUNCTUATION', ':', 34, 987), 
                   ('NEWLINE', '', 35, 988), ('INDENT', '', 35, 992), ('IDENTIFIER', 'x', 35, 994), ('OPERATOR_UNARY', '=', 35, 995), ('NUMBER', '10', 36, 999),
                   ('NEWLINE', '', 36, 999), ('IDENTIFIER', 'y', 36, 1005), ('OPERATOR_UNARY', '=', 36, 1006), ('NUMBER', '5', 37, 1009), ('NEWLINE', '', 37, 1009), 
                   ('IDENTIFIER', 'result', 39, 1079), ('OPERATOR_UNARY', '=', 39, 1080), 
                   ('IDENTIFIER', 'calcul_complexe', 39, 1097), ('PUNCTUATION', '(', 39, 1097), ('IDENTIFIER', 'x', 39, 1099), ('PUNCTUATION', ',', 39, 1099), 
                   ('IDENTIFIER', 'y', 39, 1102), ('PUNCTUATION', ')', 39, 1102), ('NEWLINE', '', 40, 1103), ('DEDENT', '', 41, 1104), 
                   ('KEYWORD', 'if', 42, 1141), ('IDENTIFIER', '__name__', 42, 1150), ('OPERATOR_BINARY', '==', 42, 1152), 
                   ('STRING', '"__main__"', 42, 1163), ('PUNCTUATION', ':', 42, 1164), ('NEWLINE', '', 43, 1165), ('INDENT', '', 43, 1169), 
                   ('IDENTIFIER', 'main', 43, 1174), ('PUNCTUATION', '(', 43, 1174), ('PUNCTUATION', ')', 43, 1175), ('NEWLINE', '', 44, 1176),
                   ('DEDENT', '', 44, 1176), ('EOF', '', 44, 1176)]

# Exécuter le test
test_lexer(code_source, expected_tokens)
