# Algoritimo Tarefa 003: Idade de um nadador (IF)
# Dev: Juan Felipe Ribas
# Data: 28.08.22

Idade = int(input("Digite a sua idade: "))

if Idade < 5:
    print("Você ainda não tem idade suficiente para ser um nadador.")
elif Idade >= 5 and Idade <= 7:
    print("Você está na categoria Infantil.")
elif Idade > 7 and Idade <= 10:
    print("Você está na categoria Juvenil.")
elif Idade > 10 and Idade <= 15:
    print("Você está na categoria Adolescente.")
elif Idade > 16 and Idade <= 30:
    print("Você está na categoria Adulto.")
else:
    print("Você está na categoria Sênior.")

