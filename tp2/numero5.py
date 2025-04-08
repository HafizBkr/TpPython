def somme(*args):
    """
    Calcule la somme des nombres contenus dans un tuple de longueur variable.

    Args:
        *args: Tuple de longueur variable contenant des nombres (entiers ou flottants)

    Returns:
        float ou int: La somme des nombres dans le tuple
    """
    resultat = 0
    for nombre in args:
        resultat += nombre
    return resultat

def main():
    # Test 1: Somme d'entiers
    resultat1 = somme(1, 2, 3, 4, 5)
    print(f"Somme de (1, 2, 3, 4, 5) = {resultat1}")

    # Test 2: Somme de flottants
    resultat2 = somme(1.5, 2.7, 3.8)
    print(f"Somme de (1.5, 2.7, 3.8) = {resultat2}")

    # Test 3: Mélange d'entiers et de flottants
    resultat3 = somme(10, 20.5, 30, 40.5)
    print(f"Somme de (10, 20.5, 30, 40.5) = {resultat3}")

    # Test 4: Un seul élément
    resultat4 = somme(42)
    print(f"Somme de (42) = {resultat4}")

    # Test 5: Aucun élément
    resultat5 = somme()
    print(f"Somme d'un tuple vide = {resultat5}")

    # Test 6: Utilisation avec unpacking de tuple
    nombres = (5, 10, 15, 20)
    resultat6 = somme(*nombres)  # Déballage du tuple
    print(f"Somme de {nombres} (par déballage) = {resultat6}")

if __name__ == "__main__":
    main()
