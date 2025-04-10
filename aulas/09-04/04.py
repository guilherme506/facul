def polindromo(n):
    junto = ''.join(n)
    inverso = junto[::-1]
    if inverso == junto:
        return 'A palavra é um polindromo'
    else:
        return 'A palavra não é um polindromo' 
print(polindromo('ovo'))