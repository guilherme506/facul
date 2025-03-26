# Percorra os número de 1 a 100 e imprima:
#
# "fuzz" se for múltiplo de 3
#
# "buzz" se for múltiplo de 5
#
# "fuzzbuzz" se for múltiplo de 3 e 5
#
# o próprio número se não se enquadrar em nenhum dos casos anteriores.
#
resultado = []
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        resultado.append('fuzzbuzz')
    elif numero % 3 == 0:
        resultado.append('fuzz')
    elif numero % 5 == 0:
        resultado.append('buzz')
    else:
        resultado.append(str(numero))
print(", ".join(resultado))
