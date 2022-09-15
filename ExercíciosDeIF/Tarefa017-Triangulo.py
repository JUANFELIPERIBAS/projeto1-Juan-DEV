# 17. Triângulo (IF)

"""
Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno.

Sendo que:

Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

print("Digite as medidas do lado do triângulo: ")

lado1 = float(input("1° lado: "))
lado2 = float(input("2° lado: "))
lado3 = float(input("3° lado: "))

if lado1 == lado2 == lado3:
    print('Este é um Triângulo Equilátero.')
elif lado1 != lado2 != lado3 and lado1 != lado3:
    print('Este é um Triângulo Escaleno.')
else:
    print('Este é um Triângulo Isóscele.')
