#exercie concernant a et b
a=0
b=10

print("Premiere boucle\n")
while a < b:
     print(f"a={a}")
     a+=1

print("deuxiem boucle\n")
while b!=0:
  b-=1
  if b % 2 != 0:
    print(f"b={b}")
