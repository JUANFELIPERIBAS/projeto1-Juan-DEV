# Algoritimo Tarefa 004: Salário bruto (IF)
# Dev: Juan Felipe Ribas
# Data: 29.08.22

Imposto = 0.07
SalarioBruto = float(input("Digite o salário bruto: "))

if SalarioBruto <= 0:
    print("Digite um valor válido.")
elif SalarioBruto <= 350:
    SalarioLiquido = SalarioBruto - (SalarioBruto * Imposto) + 100.00
    print("O salário liquido é ", SalarioLiquido)
elif SalarioBruto <= 600:
    SalarioLiquido = SalarioBruto - (SalarioBruto * Imposto) + 75.00
    print("O salário liquido é ", SalarioLiquido)
elif SalarioBruto <= 900:
    SalarioLiquido = SalarioBruto - (SalarioBruto * Imposto) + 50.00
    print("O salário liquido é ", SalarioLiquido)
else:
    SalarioLiquido = SalarioBruto - (SalarioBruto * Imposto) + 35.00
    print("O salário liquido é ", SalarioLiquido)