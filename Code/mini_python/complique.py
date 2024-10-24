# Début du programme
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

    # Affichage des résultats
    for i, res in enumerate(result):
        print(f"Résultat {i + 1}: {res}")

# Appel de la fonction principale
if __name__ == "__main__":
    main()
