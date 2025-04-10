from random import randint, choice
def funçao(a,b,c):
    soma = a + b
    multiplicaçao = a * b
    divisao = a / b
    if c == 'soma':
        return soma
    elif c == 'multiplicaçao':
        return multiplicaçao
    elif c == 'divisao':
        return divisao
print(funçao(randint(1,99), randint(1,99), choice(['multiplicaçao','soma','divisao'])))            