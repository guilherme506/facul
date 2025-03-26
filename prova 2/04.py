#Peça um número e imprima a soma de seus algarismos.
n = int(input('Digite um número: '))
lista =[int(numero) for numero in str(n)]
soma = sum(lista)

print(f'A soma do algarismo é {soma}')