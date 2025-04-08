import math

def volMasseEllipsoide(a=1.0, b=1.0, c=1.0, masse_volumique=1.0):
    """
    Calcule le volume et la masse d'un ellipsoïde.

    Args:
        a (float): Premier demi-axe de l'ellipsoïde (défaut: 1.0)
        b (float): Deuxième demi-axe de l'ellipsoïde (défaut: 1.0)
        c (float): Troisième demi-axe de l'ellipsoïde (défaut: 1.0)
        masse_volumique (float): Masse volumique de l'ellipsoïde (défaut: 1.0)

    Returns:
        tuple: Un tuple contenant (volume, masse) de l'ellipsoïde
    """
    # Calcul du volume selon la formule V = (4/3) * π * a * b * c
    volume = (4/3) * math.pi * a * b * c

    # Calcul de la masse selon la formule M = ρ * V (masse volumique * volume)
    masse = masse_volumique * volume

    return (volume, masse)

# Tests de la fonction avec différents nombres d'arguments
def main():
    # Test 1: Sans arguments (utilise les valeurs par défaut)
    vol1, masse1 = volMasseEllipsoide()
    print(f"Test 1 (valeurs par défaut):")
    print(f"Volume: {vol1:.4f}, Masse: {masse1:.4f}")

    # Test 2: Avec un seul argument - demi-axe a
    vol2, masse2 = volMasseEllipsoide(2.0)
    print(f"\nTest 2 (seulement le demi-axe a = 2.0):")
    print(f"Volume: {vol2:.4f}, Masse: {masse2:.4f}")

    # Test 3: Avec trois arguments - les trois demi-axes
    vol3, masse3 = volMasseEllipsoide(2.0, 3.0, 4.0)
    print(f"\nTest 3 (demi-axes a = 2.0, b = 3.0, c = 4.0):")
    print(f"Volume: {vol3:.4f}, Masse: {masse3:.4f}")

    # Test 4: Avec quatre arguments - les trois demi-axes et la masse volumique
    vol4, masse4 = volMasseEllipsoide(2.0, 3.0, 4.0, 2.5)
    print(f"\nTest 4 (demi-axes a = 2.0, b = 3.0, c = 4.0, masse volumique = 2.5):")
    print(f"Volume: {vol4:.4f}, Masse: {masse4:.4f}")

    # Test 5: Avec arguments nommés
    vol5, masse5 = volMasseEllipsoide(c=2.0, masse_volumique=3.0, a=1.5, b=2.5)
    print(f"\nTest 5 (arguments nommés: a = 1.5, b = 2.5, c = 2.0, masse volumique = 3.0):")
    print(f"Volume: {vol5:.4f}, Masse: {masse5:.4f}")

if __name__ == "__main__":
    main()
