# Escreva um programa que solicita a velocidade de um carro para o usuário.
#
# Caso ultrapasse 80km/h, o programa deve exibir uma mensagem dizendo que o usuário foi multado.
#
# Nesse caso, deve exibir também o valor da multa, cobrando R$5,00 para cada km/h acima de 80km/h.
velo = int(input("Qual é a velocidade do carro: "))
multa = 5 * (velo - 80)
if velo > 80:
    print("Você foi multado")
    print(f"O valor da multa é de {multa}")
else:
    print("continue andando assim")
