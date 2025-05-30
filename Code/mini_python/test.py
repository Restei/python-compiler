def operation(a, b, c):

    somme = a + b + c
    produit = a + b * c
    div = a // (b + 1)

    if a > b:
        print("a > b")
    else:
        print("a < b and a != c") 

    for i in range(a):
        print(i)
        
    lst = [a, b, c]
    lst[1]=2
    return somme 

def main():
    x = 5+5+5+5+5
    result = operation(x, y, z)
    print("Resultats:", result)
