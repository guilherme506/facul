# Peça uma palavra e imprima a quantidade de vogais e consoantes.
palavra = str(input("Digite uma palavra: ")).lower()
consoantes = "b, c, d, f, g, h, j, l, m, n, p, q, r, s, t, v, x, z"
vogais = "a, e, i, o, u"
v = 0
c = 0
for letra in palavra:
    if letra in consoantes:
        c += 1
    elif letra in vogais:
        v += 1
print(f"A quantidade de vogais é de {v} e de consoantes {c}")
