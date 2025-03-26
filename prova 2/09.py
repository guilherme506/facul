# eça os coeficientes (a, b, c) de uma equação de segundo grau e diga se as raízes são reais ou complexas.
#
# delta = b² -4ac
##Raízes reais quando delta > 0
#
# Raízes complexas quando delta < 0
a = int(input("Coeficiente A: "))
b = int(input("Coeficiente B: "))
c = int(input("coeficiente C: "))
delta = (b**2) - (4 * a * c)
if delta > 0:
    print("As raízes são reais")
else:
    print("As raízes sao complexas")
