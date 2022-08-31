# Algoritimo Tarefa 005: Empresa com 10 funcionários (While)
# Dev: Juan Felipe Ribas
# Data: 29.08.22

"""
10 funcionários
    caracteristicas dos funcionários:
        código;
        número de horas trabalhadas no mês;
        turno de trabalho:
                    M – matutino;
                    V – vespertino;
                    N – noturno.
        categoria:
                    O – operário;
                    G – gerente.

Fazer um programa que:
a) Leia as informações dos funcionários - número de horas trabalhadas - turno de trabalho - categoria
"""
Laco1 = 1
Laco2 = True
Laco3 = True

while laco1 <= 10:
    # Quadro do laço principal
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0

    Codigo = input("Digite o código do funcionário: ")
    HoraTrabalhada = float(input("Digite as horas trabalhadas: "))


