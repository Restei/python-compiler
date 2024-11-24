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
code_source = """def calcul_complexe"""

# Tokens attendus (simplifié pour l'exemple)
expected_tokens = [
    ("KEYWORD","def",1,3),
    ("IDENTIFIER","calcul_complexe",1,19),
    ('EOF', '', 1, 19)
]

# Exécuter le test
test_lexer(code_source, expected_tokens)
