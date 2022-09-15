# 11. Compra de maçâs (IF)
"""
As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia,
e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número
de maçãs compradas, calcule e escreva o valor total da compra.
"""

QteMaca = int(input("Digite a quantidade de maçãs que você deseja comprar: "))

if QteMaca < 1:
    print("Digite um valor maior ou igual a 1")
elif QteMaca < 12:
    ValorTotal = 0.3 * QteMaca
    print("O valor total é: R$", ValorTotal)
else:
    ValorTotal = 0.25 * QteMaca
    print("O valor total é: R$", ValorTotal)

