mot1=input("Entrez un mot : ")
mot2=input("Entrez un autre mot : ")
if mot1 < mot2:
    print(f"{mot1} est inférieur à {mot2}")
elif mot1 > mot2:
    print(f"{mot1} est supérieur à {mot2}")
else:
    print(f"{mot1} est égal à {mot2}")
print("Fin du programme")
