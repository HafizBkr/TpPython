import math

def cube(x):
    """
    Calcule le cube d'un nombre.

    Args:
        x (float): Le nombre dont on veut calculer le cube

    Returns:
        float: Le cube de x
    """
    return x ** 3

def volumeSphere(rayon):
    """
    Calcule le volume d'une sphère à partir de son rayon.
    Utilise la fonction cube pour calculer rayon³.

    Args:
        rayon (float): Le rayon de la sphère en unités

    Returns:
        float: Le volume de la sphère en unités³
    """
    return (4/3) * math.pi * cube(rayon)

def main():
    """Fonction principale pour tester les fonctions cube et volumeSphere."""
    # Test de la fonction cube
    test_valeur = 3
    resultat_cube = cube(test_valeur)
    print(f"Le cube de {test_valeur} est {resultat_cube}")

    # Tests de la fonction volumeSphere avec plusieurs rayons
    rayons = [1, 2, 5, 10]
    for r in rayons:
        volume = volumeSphere(r)
        print(f"Le volume d'une sphère de rayon {r} est {volume:.2f} unités³")

if __name__ == "__main__":
    main()
