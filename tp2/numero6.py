def somme (var1, var2, var3):
    return var1 + var2 + var3

def main ():
    tuple=(3,4,5)
    print(f"la somme des elements du tuple {tuple} est : {somme(*tuple)}")

if __name__ == "__main__":
    main()
