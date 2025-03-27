# gere números aleatorios de 0 a 9 e some os numeros até que o número gerado seja 0
from random import randint

soma = 0
while True:
    n = randint(0, 9)
    if n != 0:
        soma += n
    elif n == 0:
        print(f"O resultado da soma e {soma}")
        break
