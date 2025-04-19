# Création de la liste d'entiers de 0 à 5
liste_originale = list(range(6))  # [0, 1, 2, 3, 4, 5]
print("Liste originale:", liste_originale)

# Utilisation d'une liste en compréhension pour ajouter 3 à chaque élément
liste_augmentee = [x + 3 for x in liste_originale]

# Affichage du résultat
print("Liste après avoir ajouté 3 à chaque élément:", liste_augmentee)

# Explication de la syntaxe de liste en compréhension
print("\nExplication:")
print("La syntaxe [x + 3 for x in liste_originale] crée une nouvelle liste")
print("en parcourant chaque élément x de liste_originale et en ajoutant 3 à chacun.") 