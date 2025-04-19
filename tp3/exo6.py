# Création de la liste d'entiers de 0 à 9
liste = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Liste d'entiers de 0 à 9:", liste)

# Méthode 1 : Utilisation de la fonction sum()
somme1 = sum(liste)
print("\nMéthode 1 - Somme avec la fonction sum():", somme1)

# Méthode 2 : Utilisation d'une liste en compréhension avec sum()
# Cette méthode est moins efficace que la méthode 1 dans ce cas précis,
# mais montre comment utiliser une liste en compréhension
somme2 = sum([x for x in liste])
print("Méthode 2 - Somme avec liste en compréhension et sum():", somme2)

# Méthode 3 : Utilisation d'une boucle for traditionnelle
somme3 = 0
for x in liste:
    somme3 += x
print("Méthode 3 - Somme avec boucle for traditionnelle:", somme3)

# Méthode 4 : Utilisation de la fonction reduce (nécessite le module functools)
from functools import reduce
somme4 = reduce(lambda x, y: x + y, liste)
print("Méthode 4 - Somme avec reduce():", somme4)

# Note: Pour cet exercice spécifique, la méthode 1 est la plus simple et la plus efficace,
# mais l'exercice demande d'utiliser une liste en compréhension 