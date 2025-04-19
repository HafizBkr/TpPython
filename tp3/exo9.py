# Création du dictionnaire pour représenter le tableau d'informations physico-chimiques
# Les données sont basées sur l'image fournie dans l'énoncé

dico = {
    "Au": {
        "Te/Tf": [2970, 1063],
        "Z/A": [79, 196.967]
    },
    "Ga": {
        "Te/Tf": [2237, 29.8],
        "Z/A": [31, 69.72]
    }
}

# Test du dictionnaire
print("Informations physico-chimiques sur les éléments:")
print("=" * 50)

# Accès aux données
print(f"Numéro atomique (Z) de l'or (Au): {dico['Au']['Z/A'][0]}")
print(f"Masse atomique (A) de l'or (Au): {dico['Au']['Z/A'][1]}")
print(f"Température d'ébullition (Te) de l'or (Au): {dico['Au']['Te/Tf'][0]} K")
print(f"Température de fusion (Tf) de l'or (Au): {dico['Au']['Te/Tf'][1]} K")

print("\nAutres données:")
print(f"Numéro atomique (Z) du gallium (Ga): {dico['Ga']['Z/A'][0]}")
print(f"Température de fusion (Tf) du gallium (Ga): {dico['Ga']['Te/Tf'][1]} K")

# Affichage complet du dictionnaire
print("\nContenu complet du dictionnaire:")
for element, proprietes in dico.items():
    print(f"\nÉlément: {element}")
    for categorie, valeurs in proprietes.items():
        print(f"  {categorie}: {valeurs}")

# Exemple d'utilisation avec une boucle pour afficher un tableau formaté
print("\nTableau formaté des données:")
print("-" * 60)
print(f"{'Élément':^10} | {'Z':^8} | {'A':^10} | {'Te (K)':^8} | {'Tf (K)':^8}")
print("-" * 60)


for element, proprietes in dico.items():
    z, a = proprietes["Z/A"]
    te, tf = proprietes["Te/Tf"]
    print(f"{element:^10} | {z:^8} | {a:^10.3f} | {te:^8} | {tf:^8}")
print("-" * 60)
