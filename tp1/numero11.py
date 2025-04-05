import easygui as eg


def recherche_dans_liste():
        ma_liste = [2, 5, 8, 13, 21]
        nombre = eg.integerbox("Entrez un entier à rechercher dans la liste:", "Recherche")

        if nombre is not None:
            for x in ma_liste:
                if x == nombre:
                    eg.msgbox(f"Le nombre {nombre} a été trouvé dans la liste!")
                    break
            else:
                eg.msgbox(f"Le nombre {nombre} n'est pas dans la liste.")
        else:
            eg.msgbox("Recherche annulée")


def test_nombre_premier():
        n = eg.integerbox("Entrez un entier positif pour tester s'il est premier:", "Test nombre premier")

        if n is not None:
            if n > 1:
                diviseur = 2
                while diviseur * diviseur <= n:
                    if n % diviseur == 0:
                        eg.msgbox(f"{n} n'est pas premier, il est divisible par {diviseur}")
                        break
                    diviseur += 1
                else:
                    eg.msgbox(f"{n} est un nombre premier!")
            else:
                eg.msgbox(f"{n} n'est pas un nombre premier car il est inférieur ou égal à 1")
        else:
            eg.msgbox("Test de nombre premier annulé")



def main():
    recherche_dans_liste()
    test_nombre_premier()

if __name__ == "__main__":
    main()
