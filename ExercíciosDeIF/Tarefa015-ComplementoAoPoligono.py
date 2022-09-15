# 15. Complemento ao Polígono da tarefa 14 (IF)
"""
Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte:

Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
Se o número de lados for igual a 5 escrever PENTÁGONO.

Acrescente as seguintes mensagens à solução da tarefa 14 conforme o caso.

Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.

Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
"""

QteLados = int(input("Digite o número de lados do polígono: "))


#  Descobrir qual o tipo de polígono:
if QteLados < 3:
    print('NÃO É UM POLÍGONO')

elif QteLados == 3:
    print("O polígono é um TRIÂNGULO.")
    MedidaLado = float(input("Digite a medida do lado (em cm): "))
    Area = MedidaLado * MedidaLado / 2
    print("A área do triângulo é: ", round(Area, 2), "cm")

elif QteLados == 4:
    print("O polígono é um QUADRADO.")
    MedidaLado = float(input("Digite a medida do lado (em cm): "))
    Area = MedidaLado * MedidaLado
    print("A área do quadrado é: ",  round(Area, 2), "cm")

elif QteLados == 5:
    print("O polígono é um PENTÁGONO.")
elif QteLados > 5:
    print("POLÍGONO NÃO IDENTIFICADO")

'''
#  Descobrir qual a área:
if QteLados == 3:
    Area = MedidaLado * MedidaLado / 2  # considerando Triângulo retângulo a altura é =  medida do lado
    print("A área do triângulo é: ", round(Area, 2), "cm")
elif QteLados == 4:
    Area = MedidaLado * MedidaLado
    print("A área do quadrado é: ",  round(Area, 2), "cm")
'''