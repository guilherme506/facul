# Peça que um usuário digite um número.
#
# Imprima se ele é par ou impar.
#
#
# Repita o processo até que o número digitado seja 0.
while True:
    n = int(input("Digite um número: "))

    if n == 0:
        print("numero não compativel")
        break
    elif n % 2 == 0:
        print("o número e par")
    else:
        print("O número e impar ")
