import math
for x in range(-3, 4):
    try:
        resultat = math.sin(x)/x
        print(f"Pour x = {x}, sin(x)/x = {resultat}")
    except ZeroDivisionError:
        # Gestion du cas x=0 (limite de sin(x)/x quand x tend vers 0 = 1)
        print(f"Pour x = {x}, sin(x)/x = 1 (limite quand x tend vers 0)")
