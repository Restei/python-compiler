# Début du programme
def calcul_complexe(a, b):
    
    # Opérations arithmétiques de base
    somme = a + b  # Addition
    produit = a * b  # Multiplication
    division = a // b  # Division classique
    reste = a % b  # Modulo (reste de la division euclidienne)
    quotient = a // b  # Division entière


    # Opérations logiques et comparaisons
    if a == b:
        print("Les nombres sont égaux")
    if a != b:
        print("Les nombres sont différents")

    # Comparaisons binaires
    if a >= b and a <= 100:
        print("a est entre b et 100")
    if a > 0 or b < 0:
        print("Un des nombres est positif")
    return somme
  
# Fonction principale
def main():
    x = 10
    y = 5

    # Appel de la fonction avec des expressions complexes
    result = calcul_complexe(x, y)

# Appel de la fonction principale
if __name__ == "__main__":
    main()