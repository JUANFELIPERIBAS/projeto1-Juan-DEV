"""
Faça um programa que receba o salário de um funcionário chamado Carlos.
Sabe-se que outro funcionário, João, tem salário equivalente a um terço do salário de Carlos.
Carlos aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês
e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês.
O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor
pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.

"""

"""
Salário de Carlos = x
Salário de João = x/3 = y

Poupança = x * 1,02
RendaFixa = y * 1,05
"""
#var

SalarioCarlos = float(input("Digite o salário de Carlos: "))
