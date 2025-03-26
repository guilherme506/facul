# Peça duas notas que o aluno tirou no semestre.
#
# Caso a média aritmética seja maior que 6, imprima que ele está aprovado.
#
# Caso a média aritmética seja menor que 6, peça que ele digite a nota da prova de recuperação.
#
# Nesse caso, imprima a média aritmética das 3 notas e diga se ele está aprovado ou reprovado (média menor que 6).
n1 = float(input("Valor da primeira nota: "))
n2 = float(input("Valor da segunda nota: "))
nota = n1 + n2
media = (n1 + n2) / 2
if media > 6:
    print("Você esta aprovada")
if media < 6:
    print("Você esta recupeção")
    n3 = float(input("Nota da recupeção: "))
    media_final = (nota + n3) / 3
    if media_final >= 6:
        print(f"Você esta aprovada com a nota {media_final}")
    else:
        print(f"Você reprovou de ano com a nota {media_final}")
