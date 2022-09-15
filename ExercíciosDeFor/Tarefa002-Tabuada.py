# 2. Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)
"""
Faça um programa para calcular a tabuada de qualquer número digitado pelo usuário.
"""

tabuada = int(input('Digite qual a tabuada que você quer: '))
print("-" * 14)
for c in range(0, 11):
    result = tabuada * c
    print("{} x {} = {}".format(tabuada, c, result))
print("-" * 14)