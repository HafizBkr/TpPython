# Initialisation des listes
truc = []  # liste vide
machin = [0.0] * 5  # liste de cinq flottants nuls

# Affichage des listes
print("truc (liste vide):", truc)
print("machin (5 flottants nuls):", machin)

# Utilisation de la fonction range()
print("\nAffichage avec range() :")
print("Entiers de 0 à 3:")
for i in range(0, 4):
    print(i, end=" ")
print()

print("Entiers de 4 à 7:")
for i in range(4, 8):
    print(i, end=" ")
print()

print("Entiers de 2 à 8 par pas de 2:")
for i in range(2, 9, 2):
    print(i, end=" ")
print()

# Définition de chose comme liste des entiers de 0 à 5
chose = list(range(6))  # équivalent à [0, 1, 2, 3, 4, 5]
print("\nchose (liste des entiers de 0 à 5):", chose)

# Tests d'appartenance
element_3 = 3 in chose
element_6 = 6 in chose

print("Est-ce que 3 appartient à chose ?", element_3)
print("Est-ce que 6 appartient à chose ?", element_6) 