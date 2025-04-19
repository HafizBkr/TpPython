def compterMots(chaine):
    """
    Compte la fréquence de chaque mot dans une chaîne de caractères.
    
    Arguments:
        chaine (str): La chaîne de caractères à analyser
        
    Returns:
        dict: Un dictionnaire avec les mots comme clés et leurs fréquences comme valeurs
    """
    # Convertir la chaîne en minuscules pour ne pas distinguer les majuscules/minuscules
    chaine = chaine.lower()
    
    # Supprimer les caractères de ponctuation courants
    for ponctuation in ",.;:!?()[]{}\"'":
        chaine = chaine.replace(ponctuation, " ")
    
    # Diviser la chaîne en mots
    mots = chaine.split()
    
    # Créer un dictionnaire pour stocker les fréquences
    frequences = {}
    
    # Compter la fréquence de chaque mot
    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1
    
    return frequences


# Test de la fonction avec différentes chaînes
if __name__ == "__main__":
    # Test 1 : Phrase simple
    texte1 = "Bonjour le monde. Bonjour Python."
    resultat1 = compterMots(texte1)
    print("Texte 1:", texte1)
    print("Fréquence des mots:", resultat1)
    
    # Test 2 : Phrase avec ponctuation et casse variée
    texte2 = "Python est un langage de programmation. Python est facile à apprendre."
    resultat2 = compterMots(texte2)
    print("\nTexte 2:", texte2)
    print("Fréquence des mots:", resultat2)
    
    # Test 3 : Texte plus complexe
    texte3 = """L'informatique est la science du traitement de l'information.
    Elle est souvent associée à l'utilisation des ordinateurs, mais l'informatique
    couvre des domaines bien plus vastes que le simple usage des machines."""
    resultat3 = compterMots(texte3)
    print("\nTexte 3:", texte3)
    print("Fréquence des mots:")
    
    # Affichage trié par fréquence (du plus fréquent au moins fréquent)
    for mot, frequence in sorted(resultat3.items(), key=lambda x: x[1], reverse=True):
        print(f"'{mot}': {frequence}")
    
    # Méthode alternative: utiliser Counter du module collections
    print("\nMéthode alternative avec Counter:")
    from collections import Counter
    texte4 = "Python Python Python est est un langage de programmation."
    mots4 = texte4.lower().split()
    compteur = Counter(mots4)
    print(compteur) 