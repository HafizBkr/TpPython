# Définition de la liste
liste = [17, 38, 10, 25, 72]
print("Liste initiale:", liste)

# Triez et affichez la liste
liste.sort()
print("Liste triée:", liste)

# Ajoutez l'élément 12 à la liste et affichez la liste
liste.append(12)
print("Liste après ajout de 12:", liste)

# Renversez et affichez la liste
liste.reverse()
print("Liste renversée:", liste)

# Affichez l'indice de l'élément 17
print("Indice de l'élément 17:", liste.index(17))

# Enlevez l'élément 38 et affichez la liste
liste.remove(38)
print("Liste après suppression de 38:", liste)

# Affichez la sous-liste du 2e au 3e élément
print("Sous-liste du 2e au 3e élément:", liste[1:3])

# Affichez la sous-liste du début au 2e élément
print("Sous-liste du début au 2e élément:", liste[:2])

# Affichez la sous-liste du 3e élément à la fin de la liste
print("Sous-liste du 3e élément à la fin:", liste[2:])

# Affichez la sous-liste complète de la liste
print("Sous-liste complète (copie de la liste):", liste[:])

# Affichez le dernier élément en utilisant un indiçage négatif
print("Dernier élément (indice négatif):", liste[-1])

# Note : Certaines méthodes comme sort(), reverse(), append(), remove() modifient la liste en place
# et ne retournent rien (elles retournent None) 