# Variable globale pour la file
file = []

def initialiser():
    """
    Initialise la file comme une liste vide.
    """
    global file
    file = []
    print("La file a été initialisée (vidée).")

def enfiler():
    """
    Ajoute un élément à la fin de la file.
    """
    global file
    element = input("Entrez l'élément à enfiler: ")
    file.append(element)
    print(f"L'élément '{element}' a été ajouté à la file.")

def defiler():
    """
    Retire et retourne l'élément en tête de la file.
    """
    global file
    if not file:
        print("Erreur: La file est vide.")
        return
    
    element = file.pop(0)  # Retirer le premier élément (index 0)
    print(f"L'élément '{element}' a été retiré de la file.")
    return element

def afficher():
    """
    Affiche la file actuelle.
    """
    global file
    if not file:
        print("La file est vide.")
    else:
        print("Contenu de la file (de la tête à la queue):")
        for i, element in enumerate(file):
            print(f"{i+1}. {element}")
        print(f"Taille de la file: {len(file)} élément(s)")

def est_vide():
    """
    Vérifie si la file est vide.
    """
    global file
    if not file:
        print("La file est vide.")
    else:
        print("La file n'est pas vide.")
    return len(file) == 0

def menu():
    """
    Affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("\n=== MENU MANIPULATION DE FILE (FIFO) ===")
        print("1. Initialiser la file")
        print("2. Enfiler un élément")
        print("3. Défiler un élément")
        print("4. Afficher la file")
        print("5. Vérifier si la file est vide")
        print("6. Quitter")
        
        choix = input("\nVotre choix (1-6): ")
        
        if choix == "1":
            initialiser()
        elif choix == "2":
            enfiler()
        elif choix == "3":
            defiler()
        elif choix == "4":
            afficher()
        elif choix == "5":
            est_vide()
        elif choix == "6":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

# Programme principal
if __name__ == "__main__":
    print("Bienvenue dans le programme de manipulation de file (FIFO)")
    print("Une file FIFO (First In, First Out) fonctionne comme une file d'attente:")
    print("Le premier élément ajouté sera le premier à être retiré.")
    
    # Exemple d'utilisation de la file
    initialiser()
    file.extend(["premier", "deuxième", "troisième"])
    print("Exemple de file avec trois éléments:")
    afficher()
    
    # Démarrage du menu interactif
    menu() 