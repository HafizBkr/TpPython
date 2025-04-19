def pile(*elements):
    """
    Crée et retourne une pile (LIFO) à partir des éléments fournis.
    
    Arguments:
        *elements: Éléments variables à ajouter à la pile
        
    Returns:
        list: Une liste représentant la pile
    """
    return list(elements)

def empile(p, element):
    """
    Empile un élément en haut de la pile.
    
    Arguments:
        p: La pile (liste) à modifier
        element: L'élément à ajouter en haut de la pile
        
    Returns:
        None: La pile est modifiée en place
    """
    p.append(element)

def depile(p):
    """
    Dépile un élément du haut de la pile et le retourne.
    
    Arguments:
        p: La pile (liste) à modifier
        
    Returns:
        any: L'élément du haut de la pile
        
    Raises:
        IndexError: Si la pile est vide
    """
    if not p:
        raise IndexError("Impossible de dépiler une pile vide")
    return p.pop()

def est_vide(p):
    """
    Vérifie si la pile est vide.
    
    Arguments:
        p: La pile (liste) à vérifier
        
    Returns:
        bool: True si la pile est vide, False sinon
    """
    return len(p) == 0

# Programme principal pour tester les fonctions
if __name__ == "__main__":
    # Création d'une pile avec des éléments initiaux
    ma_pile = pile(1, 2, 3)
    print("Pile initiale:", ma_pile)
    
    # Empiler des éléments
    empile(ma_pile, 4)
    empile(ma_pile, 5)
    print("Pile après avoir empilé 4 et 5:", ma_pile)
    
    # Dépiler des éléments
    element = depile(ma_pile)
    print(f"Élément dépilé: {element}")
    print("Pile après avoir dépilé:", ma_pile)
    
    # Dépiler tous les éléments
    print("\nDépiler tous les éléments:")
    while not est_vide(ma_pile):
        print(f"Élément dépilé: {depile(ma_pile)}")
    
    print("Pile finale (vide):", ma_pile)
    
    # Tester le dépilage d'une pile vide (géré par une exception)
    try:
        depile(ma_pile)
    except IndexError as e:
        print(f"Erreur attendue: {e}")
    
    # Exemple d'utilisation pratique: vérification des parenthèses
    print("\nExemple d'utilisation: vérification des parenthèses")
    
    def verifier_parentheses(expression):
        p = pile()
        for char in expression:
            if char == '(':
                empile(p, char)
            elif char == ')':
                try:
                    depile(p)
                except IndexError:
                    return False
        return est_vide(p)
    
    expressions = ["(a+b)", "(a+b)*(c-d)", "(a+(b-c)", "a+b)"]
    for expr in expressions:
        resultat = verifier_parentheses(expr)
        print(f"Expression '{expr}' a des parenthèses équilibrées: {resultat}") 