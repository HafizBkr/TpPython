
from enum import EnumMeta


ma_liste=["Anna",17,"Feminin","Ali","Prof",19]

# print(ma_liste[0:2]) #1
# print(ma_liste[1:3]) #2
# print(ma_liste[1:4]) #3
# print(ma_liste[0:5:2]) #4
# print(ma_liste[0:2])  #5
# print(ma_liste[2:5:2]) #6
# print(ma_liste[3::2]) #7
# print(ma_liste[4:6]) #8
# print(ma_liste[1::2]) #9

# print(ma_liste[2::3]) #dernier


# for i in range (len(ma_liste)):
#     print(f"{i+1}, {ma_liste[i]}")

# for i ,el in enumerate(ma_liste):
#    print(f"{i+1}, {[el]}")

index =0
for i in ma_liste:
    index+=1
    print(f" {index}:{i} ")
