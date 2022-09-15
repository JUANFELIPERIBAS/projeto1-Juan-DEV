# 14. Polígono (IF)
"""
Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte:

Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
Se o número de lados for igual a 5 escrever PENTÁGONO.
"""

QteLados = int(input("Digite o número de lados do polígono: "))
MedidaLado = float(input("Digite a medida do lado (em cm): "))

#  Descobrir qual o tipo de polígono:
if QteLados == 3:
    print("O polígono é um TRIÂNGULO.")
elif QteLados == 4:
    print("O polígono é um QUADRADO.")
elif QteLados == 5:
    print("O polígono é um PENTÁGONO.")
else:
    print("Digite valores entre 3 e 5")

#  Descobrir qual a área:
if QteLados == 3:
    Area = MedidaLado * MedidaLado / 2  # considerando Triângulo retângulo a altura é =  medida do lado
    print("A área do triângulo é: ", round(Area, 2), "cm")
elif QteLados == 4:
    Area = MedidaLado * MedidaLado
    print("A área do quadrado é: ",  round(Area, 2), "cm")
