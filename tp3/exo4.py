# Création de la liste d'entiers de 0 à 5
liste_originale = list(range(6))  # [0, 1, 2, 3, 4, 5]
print("Liste originale:", liste_originale)

# Utilisation d'une liste en compréhension avec condition
# Ajouter 3 seulement aux éléments supérieurs ou égaux à 2
liste_conditionnelle = [x + 3 for x in liste_originale if x >= 2]

# Affichage du résultat
print("Liste après avoir ajouté 3 aux éléments >= 2:", liste_conditionnelle)

# Alternative : garder tous les éléments mais n'ajouter 3 qu'à ceux >= 2
liste_alternative = [x + 3 if x >= 2 else x for x in liste_originale]
print("Alternative (tous les éléments mais n'ajouter 3 qu'à ceux >= 2):", liste_alternative)

# Explication de la syntaxe
print("\nExplication:")
print("La syntaxe [x + 3 for x in liste_originale if x >= 2] crée une nouvelle liste")
print("en ne conservant que les éléments x de liste_originale qui sont >= 2,")
print("puis en ajoutant 3 à chacun de ces éléments.") 