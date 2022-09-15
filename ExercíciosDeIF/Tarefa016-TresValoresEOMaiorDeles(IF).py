# 16. Três valores e o maior deles (IF)
"""
Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
Considere que o usuário não informará valores iguais.
"""

Valor1 = int(input("Digite o 1º valor: "))
Valor2 = int(input("Digite o 2º valor: "))
Valor3 = int(input("Digite o 3º valor: "))

if Valor1 > Valor2 and Valor1 > Valor3:
    print(f'O maior valor digitado é {Valor1}')
elif Valor2 > Valor1 and Valor2 > Valor3:
    print(f'O maior valor digitado é {Valor2}')
else:
    print(f'O maior valor digitado é {Valor3}')
