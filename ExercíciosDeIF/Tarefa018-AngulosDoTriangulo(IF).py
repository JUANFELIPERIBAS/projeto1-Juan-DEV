# 18. Ângulos do triângulo (IF)

"""
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva
se o triângulo é Acutângulo, Retângulo ou Obtusângulo.
Sendo que:
Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
TriânguloAcutângulo: possui três ângulos agudos. (menor que 90º
"""
print("Digite o valor dos ângulos de um triângulo: ")

ang1 = int(input("1° ângulo(°): "))
ang2 = int(input("2° ângulo(°): "))
ang3 = int(input("3° ângulo(°): "))

if ang1 + ang2 + ang3 != 180:
    print('A soma dos ângulos de um triângulo precisa ser igual a 180°.')
elif ang1 == 0 or ang2 == 0 or ang3 == 0:
    print('Digite um valor diferente de zero para cada ângulo.')
elif ang1 == 90 or ang2 == 90 or ang3 == 90:
    print('Este tipo de triângulo é um triângulo Retângulo.')
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print('Este tipo de triângulo é um triângulo Obtusângulo.')
elif ang1 < 90 and ang2 < 90 and ang3 < 90:
    print('Este tipo de triângulo é um triângulo Acutângulo.')
