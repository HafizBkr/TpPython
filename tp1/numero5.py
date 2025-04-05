while True:
    try:
        nombre = int(input("Entrez un nombre entre 1 et 10 : "))
        if 1 <= nombre <= 10:
            print(f"Vous avez entré le nombre {nombre}")
            break
        else:
            print("Erreur : le nombre doit être entre 1 et 10")
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide")
