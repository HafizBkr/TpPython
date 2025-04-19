# Programme pour calculer les moyennes et déterminer le classement des étudiants
"""
Variables pour stocker les donneer
j'ai fixer le  nombre d'etudiant a 7
et j'utilise des tableau pour stocker  les moyenes et les numeros des etudiants
"""
nombre_etudiants = 7
moyennes = []
numeros_etudiants = []

print("=== CALCUL DES MOYENNES ET CLASSEMENT DES ETUDIANTS ===")

# Saisie des notes pour chaque etudiant
for i in range(nombre_etudiants):
    print(f"\nSaisie des notes pour l'étudiant {i+1}:")

    # Récupération des 3 notes
    somme_notes = 0
    for j in range(3):
        while True:
            try:
                note = float(input(f"Entrez la note {j+1} (sur 20): "))
                if 0 <= note <= 20:
                    somme_notes += note
                    break
                else:
                    print("Erreur: La note doit être comprise entre 0 et 20.")
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide.")

    # Calcul de la moyenne
    moyenne = somme_notes / 3

    # Stockage des informations
    moyennes.append(moyenne)
    numeros_etudiants.append(i+1)

# Affichage des moyennes
print("\n=== RÉCAPITULATIF DES MOYENNES ===")
for i in range(nombre_etudiants):
    print(f"Étudiant {numeros_etudiants[i]}: Moyenne = {moyennes[i]:.2f}/20")

# Recherche du premier et du dernier de la classe
meilleure_moyenne = max(moyennes)
pire_moyenne = min(moyennes)

index_premier = moyennes.index(meilleure_moyenne)
index_dernier = moyennes.index(pire_moyenne)

# Affichage du classement
print("\n=== CLASSEMENT ===")
print(f"Premier de la classe: Étudiant {numeros_etudiants[index_premier]} avec une moyenne de {meilleure_moyenne:.2f}/20")
print(f"Dernier de la classe: Étudiant {numeros_etudiants[index_dernier]} avec une moyenne de {pire_moyenne:.2f}/20")

"""dans une version plus améliorée on aurait pu aller jusqu'a
   demander les noms des etudiants mais  bon ce serait abuser
   j'aurai rajouter une variable noms=[]
   et pour saisir les nom sa aurai ressembler a sa

   nombre_etudiants = 7
   noms = []
      for i in range(1, nombre_etudiants + 1):
       print(f"\nÉtudiant {i}:")

       # Saisie du nom
       nom = input("  Entrez le nom de l'étudiant: ")
       noms.append(nom)
"""
