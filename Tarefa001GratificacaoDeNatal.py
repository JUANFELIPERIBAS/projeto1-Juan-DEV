# Algoritimo Tarefa 001: Gratificação de natal (IF)
# Dev: Juan Felipe Ribas
# Data: 28.08.22

"""
números não inteiros são definidos por "." e não ","!!
"""
HorasExtras = float(input("Digite o número de horas extras: "))
HorasFaltas = float(input("Digite o número de horas Faltantes: "))

TotalMinutos = (HorasExtras - (2/3*HorasFaltas)) * 60

if TotalMinutos > 2400:
    print("Os minutos totais são: ", TotalMinutos, "com gratificação de R$ 500,00")
elif TotalMinutos > 1800 and TotalMinutos <= 2400:
    print("Os minutos totais são: ", TotalMinutos, "com gratificação de R$ 400,00")
elif TotalMinutos > 1200 and TotalMinutos <= 1800:
    print("Os minutos totais são: ", TotalMinutos, "com gratificação de R$ 300,00")
elif TotalMinutos >= 600 and TotalMinutos <= 1200:
    print("Os minutos totais são: ", TotalMinutos, "com gratificação de R$ 200,00")
elif TotalMinutos <600:
    print("Os minutos totais são: ", TotalMinutos, "com gratificação de R$ 100,00")