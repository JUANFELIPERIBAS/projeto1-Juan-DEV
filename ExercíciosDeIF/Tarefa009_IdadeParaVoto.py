# 9. Idade para voto (IF)

"""
Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma
mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês
em que ela nasceu).
"""

AnoNascimento = int(input("Digite o ano do seu nascimento: "))
AnoAtual = int(input("Digite o ano atual: "))

Idade = (AnoAtual - AnoNascimento)
if Idade < 1 or Idade > 120:
    print("A idade informada precisa ser maior que 1 ano e menor que 120 anos.")
else:
    print("Sua idade é:", Idade, "anos")

if 1 <= Idade < 16:
    print("Você ainda não pode votar")
elif 16 <= Idade < 18 or 70 < Idade <= 120:
    print("Seu voto é facultativo")
elif 16 <= Idade < 70:
    print("Você é obrigado(a) a votar")

