# Définition des ensembles
X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}

# Affichage des ensembles initiaux
print("Ensemble X:", X)
print("Ensemble Y:", Y)

# Tests d'appartenance
print("\nTests d'appartenance:")
print("'c' appartient à X ?", 'c' in X)
print("'a' appartient à Y ?", 'a' in Y)

# Différence d'ensembles
print("\nDifférences d'ensembles:")
print("X - Y =", X - Y)  # Éléments dans X mais pas dans Y
print("Y - X =", Y - X)  # Éléments dans Y mais pas dans X

# Union d'ensembles (∪)
union = X.union(Y)  # ou X | Y
print("\nUnion X ∪ Y =", union)

# Intersection d'ensembles (∩)
intersection = X.intersection(Y)  # ou X & Y
print("Intersection X ∩ Y =", intersection)

# Autres opérations sur les ensembles (hors sujet mais utiles)
print("\nAutres opérations sur les ensembles:")
print("Différence symétrique X △ Y =", X.symmetric_difference(Y))  # ou X ^ Y
print("X est-il un sous-ensemble de Y ?", X.issubset(Y))
print("X est-il un sur-ensemble de Y ?", X.issuperset(Y)) 