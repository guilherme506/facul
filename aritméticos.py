#Operadores Aritméticos

# + adição
# - subtração
# * multiplicação
# / divição
# ** potêncis
# // divisão inteira
# % resto da divisão

5 + 2 == 7 
5 - 2 == 3 
5 * 2 == 10 
5 / 2 == 2.5 
5 ** 2 == 25 
5 // 2 == 2 
5 % 2 == 1 

#ordem de precadência
#1 -(), 2- **, 3- */,%,/,/, 4- +,-

#exercicios 
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)
nome = input('qual é o seu nome? ')
print('prazer em te conhecer {:=^20}!'.format(nome))
# >=centraliza pra direita
# <=centraliza pra esquerda
# ^centraliza pro centro
# ==coloca iguais em volta

n1 = int(input('digite um valor que desejas: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} , o produto é {} e a divisão é {}'.format(s,m,d), end='')
print(' A divisão inteira é {} é a potência {}'.format(di,e))
#para quebrar após o print /n 
#para não quebrar end=' '

#DESAFIOS
#primeiro desafio criar um programa que fale o sucessor e o antecessor de qaulquer numero
an = int(input('digite um numero: '))
i = an + 1
u = an - 1
print('o valor numero é {}, seu antecessor é {} e o seu sucessor é {}'.format(an,u,i))

#segundo crie um programa que fale o dobro,triplo e a raiz quadrada de qualquer numero 
aq = int(input('digite um numero: '))
w = aq * 2
wq = aq * 3
we = aq // 2
print('o dobro do numero é {}, o triplo é {} e a raiz quadrada é {}'.format(w,wq,we))

#terceiro desenvolva um programa que leia as duas notas de um aluno,calcule e mostre sua media

az = int(input('digite a primeira nota: '))
ad = int(input('digite a segunda nota: '))
ax = (ad+az)/2
print('A média do aluno é {}'.format(ax))

#quarto: escreva um programa que leia um valor em metro e o exiba convertido a milimetros 

sx = float(input('quantos metros: '))
sc = sx * 100
sv = sx * 1000
print('{} metros tem {} centímetros ou {} milímetros'.format(sx,sc,sv))

#quinto: faça um programa que leia um número inteiro qualquer e mostre sua tabuada

tabuada = int(input('qual numero de tabuada vc quer? '))
