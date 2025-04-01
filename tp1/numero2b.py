
mot1=input("Entrez un mot : ")
mot2=input("Entrez un autre mot : ")
res = f"{mot1} est inférieur à {mot2}" if mot1 < mot2 else f"{mot1} est supérieur à {mot2}" if mot1 > mot2 else f"{mot1} est égal à {mot2}"
print(res)
print("Fin du programme")
