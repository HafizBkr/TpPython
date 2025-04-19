# Définition des chaînes de caractères
chaine1 = "abc"
chaine2 = "de"

# Utilisation d'une liste en compréhension avec deux boucles for imbriquées
liste_combinaisons = [x + y for x in chaine1 for y in chaine2]

# Affichage du résultat
print(f"Combinaisons des caractères de '{chaine1}' et '{chaine2}':")
print(liste_combinaisons)

# Explication de la syntaxe
print("\nExplication:")
print("La syntaxe [x + y for x in chaine1 for y in chaine2] crée une liste")
print("en combinant chaque caractère x de chaine1 avec chaque caractère y de chaine2.")
print("C'est équivalent à:")
print("resultat = []")
print("for x in chaine1:")
print("    for y in chaine2:")
print("        resultat.append(x + y)")

# Démonstration avec la méthode traditionnelle
print("\nMéthode traditionnelle (sans liste en compréhension):")
resultat_traditionnel = []
for x in chaine1:
    for y in chaine2:
        resultat_traditionnel.append(x + y)
print(resultat_traditionnel) 