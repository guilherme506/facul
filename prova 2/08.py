#Peça que o usuário digite seu nome completo e imprima cada nome em uma linha.

nome = str(input('Digite seu nome completo: '))
n = nome.split()
for palavra in n:
        print('____________')
        print(palavra)