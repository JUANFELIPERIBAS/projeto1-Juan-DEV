"""
Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.
"""

Valor1 = float(input("Digite o 1º valor: "))
Valor2 = float(input("Digite o 2º valor: "))

if Valor1 > Valor2:
    print("O maior valor entre os 2 que você digitou é: ",Valor1)
elif Valor2 > Valor1:
    print("O maior valor entre os 2 que você digitou é: ", Valor2)
else:
    print("Os 2 valores informados não podem ser iguais")

