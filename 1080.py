from ast import Index
import random
list = []
contador = 1
numero = int(input())
while contador <= 5:
    n = int(input())
    print(n)
    list.append(n)
    contador = contador + 1
maxi = max(list)
print("---------------------------------")
print(maxi)
print(list.index(maxi))
