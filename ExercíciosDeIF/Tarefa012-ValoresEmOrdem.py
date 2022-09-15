# 12. 3 valores em ordem (IF)
"""
Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais)
e escrevê-los em ordem crescente.
"""

Valor1 = int(input("Digite o 1º valor: "))
Valor2 = int(input("Digite o 2º valor: "))
Valor3 = int(input("Digite o 3º valor: "))

if Valor1 == Valor2 or Valor1 == Valor3 or Valor2 == Valor3:
    print("Os valores digitados não podem ser iguais!")
elif Valor1 < Valor2 < Valor3:
    print("Reorganizando em ordem crescente: ", Valor1, ",", Valor2, ",", Valor3)
elif Valor1 < Valor3 < Valor2:
    print("Reorganizando em ordem crescente: ", Valor1, ",", Valor3, ",", Valor2)
elif Valor2 < Valor1 < Valor3:
    print("Reorganizando em ordem crescente: ", Valor2, ",", Valor1, ",", Valor3)
elif Valor2 < Valor3 < Valor1:
    print("Reorganizando em ordem crescente: ", Valor2, ",", Valor3, ",", Valor1)
elif Valor3 < Valor2 < Valor1:
    print("Reorganizando em ordem crescente: ", Valor3, ",", Valor2, ",", Valor1)
elif Valor3 < Valor1 < Valor2:
    print("Reorganizando em ordem crescente: ", Valor3, ",", Valor1, ",", Valor2)
