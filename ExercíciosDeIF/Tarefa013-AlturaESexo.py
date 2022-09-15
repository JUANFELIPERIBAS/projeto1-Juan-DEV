#  13. Altura e sexo (IF)

"""
Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino)
de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:

para homens: (72.7 * Altura) – 58
para mulheres: (62.1 * Altura) – 44.7
"""

Altura = float(input("Digite a sua altura: "))
Sexo = int(input("Digite o sexo (sendo 1 para feminino e 2 para masculino): "))

if Sexo == 1:
    PesoIdeal = (62.1 * Altura) - 44.7
    print("O peso ideal para o sexo Feminino com a altura de ", Altura, "metros é: ", round(PesoIdeal, 2))
elif Sexo == 2:
    PesoIdeal = (72.7 * Altura) - 58
    print("O peso ideal para o sexo Masculino com a altura de ", Altura, "metros é: ", round(PesoIdeal, 2))
else:
    print("Digite 1 para sexo feminino ou 2 para sexo masculino.")
