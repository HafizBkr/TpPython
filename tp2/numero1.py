def table(base, debut, fin, inc):
    """
    Affiche la table de multiplication du nombre base,
    de debut à fin, avec un incrément inc.

    Args:
        base (int): Le nombre dont on affiche la table
        debut (int): Valeur de départ
        fin (int): Valeur de fin
        inc (int): Incrément entre chaque valeur
    """
    i = debut
    while i <= fin:
        print(f"{base} × {i} = {base * i}")
        i += inc

def main ():
    print("Table de 7, de 3 à 15, de 2 en 2:")
    table(7, 3, 15, 2)

    print("\nTable de 9, de 1 à 10, de 1 en 1:")
    table(9, 1, 10, 1)
# Programme principal pour tester la procédure
if __name__ == "__main__":
   main()
