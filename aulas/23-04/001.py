# Dado o dicionário ao lado, imprima os seguintes dados:
 
# Quantos alunos existem?
# Alguém tirou nota zero?
# Qual foi a menor nota?
# Qual foi a maior nota?
 
alunos = {
    "Alice": 8.5,
    "Bruno": 7.8,
    "Carla": 9.2,
    "Diego": 6.9,
    "Eva": 8.0,
    "Fernando": 7.5,
    "Gabriela": 9.0,
    "Henrique": 6.7,
    "Isabela": 8.3,
    "João": 7.2
}
print(len(alunos))
for valor in alunos.values():
    if valor == 0:
        print(valor)
    else:
        print('Não tem alunos com a nota zero')
        break
print(max(alunos.values()))
print(min(alunos.values()))