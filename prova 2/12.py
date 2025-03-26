#   Dada uma lista:
#
# lista = [50, 30, 70, 80, 10]
#
# Imprima o maior valor da lista.
#
# Imprima o menor valor da lista.
#
# Imprima o somatório de todos os números da lista.
#
# mprima a lista ordenada em ordem crescente.
lista = [50, 30, 70, 80, 10]
maior = max(lista)
menor = min(lista)
soma = sum(lista)
lista.sort()
print(f"O maior valor da lista é {maior}")
print(f"O menor valor da lista é {menor}")
print(f"A soma dos valores da lista é {soma}")
print(f"A lista em ordem crescente é {lista}")
