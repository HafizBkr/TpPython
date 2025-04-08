def  unDictionnaire (**dictionaire):
   print("voici se qu'un dictionaire contient:")
   for cle , valeur in dictionaire.items():
      print(f"clé: {cle}, valeur: {valeur}")


def main():
    dictionaire = {
        "nom": "BOUKARI",
        "age": 30,
        "ville": "New York",
        "pays": "USA",
        "profession": "Ingénieur",
        "experience": 5,
        "langues": ["Anglais", "Espagnol"],
        "hobbies": ["Football", "Musique"]
    }
    unDictionnaire(**dictionaire)

if __name__ == "__main__":
    main()
