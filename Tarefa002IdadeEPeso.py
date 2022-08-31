# Algoritimo Tarefa 002: Idade e peso (IF)
# Dev: Juan Felipe Ribas
# Data: 28.08.22

#Variáveis
Idade = int(input("Digite a sua idade: "))
Peso = float(input("Digite o seu peso: "))

if Idade < 20 and Peso < 60:
    print("Com", Idade,"anos e no peso de", Peso,"kG, você está no grupo de risco 9")
elif Idade < 20 and 60 <= Peso <= 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 8")
elif Idade < 20 and Peso > 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 7")
elif Idade >= 20 and Idade <= 50 and Peso < 60:
    print("Com", Idade,"anos e no peso de", Peso,"kG, você está no grupo de risco 6")
elif Idade >= 20 and Idade <= 50 and Peso >= 60 and Peso <= 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 5")
elif Idade >= 20 and Idade <= 50 and Peso > 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 4")
elif Idade > 50 and Peso < 60:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 3")
elif Idade > 50 and Peso >= 60 and Peso <= 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 2")
elif Idade > 50 and Peso > 90:
    print("Com", Idade, "anos e no peso de", Peso, "kG, você está no grupo de risco 1")
