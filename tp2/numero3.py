import easygui as eg
import numpy as np

def maFonction(x):
    """
    Calcule la valeur de f(x) = 2x³ + x - 5

    Args:
        x (float): La valeur de x

    Returns:
        float: La valeur de f(x)
    """
    return 2 * x**3 + x - 5

def tabuler(fonction, borneInf, borneSup, nbPas):
    """
    Affiche un tableau de valeurs d'une fonction entre deux bornes.

    Args:
        fonction (callable): La fonction à tabuler
        borneInf (float): Borne inférieure
        borneSup (float): Borne supérieure
        nbPas (int): Nombre de pas entre les bornes

    Returns:
        str: Tableau formaté des valeurs de la fonction
    """
    # Vérification que borneInf < borneSup
    if borneInf >= borneSup:
        return "Erreur: La borne inférieure doit être strictement inférieure à la borne supérieure."

    # Calcul du pas
    pas = (borneSup - borneInf) / nbPas

    # Utilisation de numpy pour générer les valeurs de x efficacement
    x_values = np.linspace(borneInf, borneSup, nbPas + 1)

    # Construction du tableau de résultats
    result = "x\t|\tf(x)\n" + "-" * 30 + "\n"

    # Vectorisation pour calculer les valeurs de f(x) efficacement
    y_values = fonction(x_values)

    # Construction du tableau formaté
    for i in range(len(x_values)):
        result += f"{x_values[i]:.4f}\t|\t{y_values[i]:.4f}\n"

    return result

def main():
    """
    Programme principal qui demande les bornes et le nombre de pas,
    puis affiche le tableau de valeurs.
    """
    # Saisie des bornes et du nombre de pas avec easygui
    msg = "Entrez les paramètres pour tabuler la fonction f(x) = 2x³ + x - 5"
    title = "Tabulation de fonction"

    # Saisie des bornes
    fieldNames = ["Borne inférieure", "Borne supérieure"]
    fieldValues = eg.multenterbox(msg, title, fieldNames)

    if fieldValues is None:  # L'utilisateur a annulé
        return

    try:
        borneInf = float(fieldValues[0])
        borneSup = float(fieldValues[1])
    except ValueError:
        eg.msgbox("Les bornes doivent être des nombres.", "Erreur")
        return

    # Saisie du nombre de pas
    nbPas = eg.integerbox("Nombre de pas", title, default=10, lowerbound=1, upperbound=1000)

    if nbPas is None:  # L'utilisateur a annulé
        return

    # Appel de la procédure tabuler et affichage du résultat
    resultat = tabuler(maFonction, borneInf, borneSup, nbPas)
    eg.textbox("Tableau des valeurs", title, resultat, codebox=True)

if __name__ == "__main__":
    main()
