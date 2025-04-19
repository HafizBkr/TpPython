#initialisation des
nombre_etudiants = 7
nombre_notes = 3

# Listes pour stocker les informations des étudiants
noms = []
moyennes = []

# Fonction pour vérifier si une note est valide
def verifier_note(note):
    return 0 <= note <= 20

# fonction de clacul de notes
for i in range(1, nombre_etudiants + 1):
    print(f"\nÉtudiant {i}:")

    # Saisie du nom
    nom = input("  Entrez le nom de l'étudiant: ")
    noms.append(nom)

    total = 0
    for j in range(1, nombre_notes + 1):
        while True:
            try:
                note = float(input(f"  Entrez la note {j} (sur 20): "))
                if verifier_note(note):
                    total += note
                    break
                else:
                    print("  Erreur: La note doit être comprise entre 0 et 20.")
            except ValueError:
                print("  Erreur: Veuillez entrer un nombre valide.")

    moyenne = total / nombre_notes
    moyennes.append(moyenne)

# Affichage des moyennes
print("\nMoyennes des étudiants:")
for i in range(nombre_etudiants):
    print(f"  {noms[i]}: Moyenne = {moyennes[i]:.2f}")

# Affichage du premier et du dernier étudiant
print(f"\nPremier étudiant: {noms[0]} - Moyenne = {moyennes[0]:.2f}")
print(f"Dernier étudiant: {noms[-1]} - Moyenne = {moyennes[-1]:.2f}")
