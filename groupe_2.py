import random

    #-----------------------------------------------------#
    #                                                     #
    #                                                     #
    #                MISSION: Code Secret                 #
    #                                                     #
    #                                                     #
    # ----------------------------------------------------#
    #AUTEURS:
    #~BOUKARI Hafiz
    #~PEIRERA Salim
    #~MATCHAME Kevin
    #~DAMATA SANTANA Cedric
    #~EPUH Rodrigue

"""
  Fonction pour generer un nombre aleatoire entre 1 a 50
"""
def generer_nombre_magique():
    return random.randint(1, 50)

"""
 fonction pour trouver le nombre aleatoire
 generer par ma fonction generer_nombre_magique
"""

def troouver_nombre_aleatoire(nombre_magique, proposition):
    if proposition < nombre_magique:
        return "Trop petit"
    elif proposition > nombre_magique:
        return "Trop grand"
    else:
        return "Correct"

"""
fonction pricipale pour  jouer !!
"""
def jouer():
    #variable nombre_magique pour aceuillir le nombre generer aleatoirement
    nombre_magique = generer_nombre_magique()
    essais_restants = 7
    borne_min = 1
    borne_max = 50

    print("Amegan Bienvenue dans le jeu !")
    print("Amegan Devine un nombre entre 1 et 50. Vous avez 7 tentatives. si non on vas tegbra")

    while essais_restants > 0:
        try:
            proposition = int(input(f"Entrez un nombre ({borne_min}-{borne_max}): "))
        except ValueError:
            print("Amegan entrer un nombre valide.")
            continue

        resultat = troouver_nombre_aleatoire(nombre_magique, proposition)

        if resultat == "Correct":
            print(f"Bravo ! Amegan tu as trouver le nombre magique en {7 - essais_restants + 1} essai(s) !")
            return
        else:
            print(resultat)
            essais_restants -= 1

            # Reductionde la foruchete
            if resultat == "Trop petit" and proposition > borne_min:
                borne_min = proposition + 1
            elif resultat == "Trop grand" and proposition < borne_max:
                borne_max = proposition - 1

            print(f"Il vous reste {essais_restants} tentative(s) Amegan!!!.")

    print(f"Tu as rattterrrrr... Le nombre magique était {nombre_magique}.")

#Programe principale
if __name__ == "__main__":
    #Rappel de la fonction pricipale
    jouer()
