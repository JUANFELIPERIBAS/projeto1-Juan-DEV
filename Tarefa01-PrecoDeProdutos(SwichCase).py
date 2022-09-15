# 1 - Estruturas condicionais e de repetição: Preço de produtos (Swich Case)

preco = float(input("Digite o valor do produto: "))
cat = int(input("Digite a categoria do produto: "))
situacao = str(input("Digite a situação do produto: "))


# Valor do aumento -------------------------------------------
if 0 < preco <= 25:
    if cat == 1:
        aumento = (preco * 1.05) - preco
        print("O valor do aumento para este produto é: R$", aumento)
    elif cat == 2:
        aumento = (preco * 1.08) - preco
        print("O valor do aumento para este produto é: R$", round(aumento, 2))
    elif cat == 3:
        aumento = (preco * 1.1) - preco
        print("O valor do aumento para este produto é: R$", round(aumento, 2))
    else:
        print("Digite a categoria 1 para limpeza, 2 para alimentação ou 3 para vestuário. ")

else:
    if cat == 1:
        aumento = (preco * 1.12) - preco
        print("O valor do aumento para este produto é: R$", round(aumento, 2))
    elif cat == 2:
        aumento = (preco * 1.15) - preco
        print("O valor do aumento para este produto é: R$", round(aumento, 2))
    elif cat == 3:
        aumento = (preco * 1.18) - preco
        print("O valor do aumento para este produto é: R$", round(aumento, 2))
    else:
        print("Digite a categoria 1 para limpeza, 2 para alimentação ou 3 para vestuário. ")

# Valor do imposto------------------------------------------------------

if cat == 2 or situacao == "R":
    imposto = (preco * 1.05) - preco
    print("O valor do imposto a ser pago é: R$", round(imposto,2))
else:
    imposto = (preco * 1.08) - preco
    print("O valor do imposto a ser pago é: R$", round(imposto,2))

# Novo preço-----------------------------------------------------------

novoPreco = preco + aumento
print("o novo preço para este produto é: ", round(novoPreco,2))

# Classificação-------------------------------------------------------

if novoPreco <= 50:
    print("Classificação do produto: Barato.")
elif novoPreco < 120:
    print("Classificação do produto: Normal.")
else:
    print("Classificação do produto: Caro.")
