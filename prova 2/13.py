#Peça que o usuário digite um número e digite Enter.
#
#Enquanto o número digitado for maior que 0, vá somando esses números.
#
#Quando o número digitado for zero, interrompa o programa e imprima o somatório dos números digitados.
soma = 0
while True:
     n = int(input('Digite um número(se quiser parar digite 0): '))
     if n != 0:
        soma += n
     elif n == 0:
        print(f'O resultado deu {soma}')
        break