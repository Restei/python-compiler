def operation(a, b, c):
    # Opérations simples , associativité et priorité des opérateurs
    somme = a + b - c
    produit = a + b * c
    div = a / (b + 1)
    
    # Comparaison et condition
    if a > b:
        print("a > b")
    elif a == c:
        print("a == c")
    else:
        
        print("a < b and a != c") 
        

    # Boucle
    for i in range(a):
        prin(i) # Erreur syntaxique : print mal orthographié

    # Liste
    lst = [a, b, c]
    

    # Retour des résultats
    return somme, produit, div, lst

def main():
    x = 5
    y = 3
    z = 7

    result = operation(x, y, z)
    print("Resultats:", result)

if __name__ == "__main__":
    main()
