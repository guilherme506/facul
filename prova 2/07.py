# Peça que o usuário digite uma palavra e imprima quantas vezes cada letra se repete.
palavra =  (input("Digite uma palavra: ")).lower()
contador = {}
for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1
print("\nfrequência das letras: ")
for letra, quantidade in contador.items():
    print(f"A a letra {letra}, apareceu {quantidade} vezes")
