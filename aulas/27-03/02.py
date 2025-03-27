# gere 10 numeors aleatorios de 0 a 1000 . se n for multiplo de 10, inprima lows. senão imprima m. Emprima a soma dos m
# o menor valor dos m e o maior valor dos m
from random import randint

lista = []
for numero in range(10):
    n = randint(0, 1000)
    if n % 10 == 0:
        print("bows")
    else:
        print(n)
    lista.append(n)
print(sum(lista), max(lista), min(lista))
