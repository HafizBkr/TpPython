pSeuil = 2.3
vSeuil = 7.41

# Première saisie
volume = float(input("Enter volume: "))
pression = float(input("Enter pressure: "))

while True:
    if pression > pSeuil and volume > vSeuil:
        print("arret imediat")
        print(f"volume: {volume}, pression: {pression}")
        break
    elif pression > pSeuil:
        print("Attention, pression trop elevee veuillez augmenter le volume")
        volume = float(input("Enter volume: "))
    elif volume > vSeuil:
        print("Attention, volume trop eleve veuillez le diminuer")
        volume = float(input("Enter volume: "))
    else:
        print("tout vas bien")
        print(f"volume: {volume}, pression: {pression}")
        break
