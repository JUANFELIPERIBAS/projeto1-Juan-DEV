# 1. Estruturas condicionais e de repetição: Aumento salarial (FOR)
"""
Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;
b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;
c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017. Apresente todos os valores.
"""
anoInicial = 2000
anofinal = 2017
salarioIni = 1000
aumento = 0.015
salario = (aumento + 1) * salarioIni
print("Em {} o salário foi: R$ {}".format(anoInicial, round(salarioIni, 2)))
print("Em {} o percentual de aumento foi de {} % com um salário de R$ {}".format(anoInicial + 1,
                                                                                 aumento * 100, round(salario, 2)))

for anos in range(anoInicial + 2, anofinal + 1):
    aumento = aumento * 2
    salario = salario + (salario * aumento)
    print("Em {} o percentual de aumento foi de {} % com um salário de R$ {}".format(anos, aumento * 100,
                                                                                     round(salario, 2)))
