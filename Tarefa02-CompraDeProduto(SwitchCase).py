# 2. Estruturas condicionais e de repetição: Compra de produto (Switch Case)

codigo = int(input("Digite o código do produto: "))
qte = int(input("Digite a quantidade do produto: "))

if 1 <= codigo <= 10:
    preco = 10.00
    totalNota = preco * qte
    if totalNota <= 250:
        desconto = totalNota * 0.05
        precoFinal = totalNota - desconto
        print("=-" * 23)
        print("Preço unitário: R$ {} \nPreço total da nota: R$ {} \nValor do desconto: R$ {} \n"
              "Preço final da nota após o desconto: R$ {} ".format(preco, totalNota, desconto, precoFinal))
        print("=-" * 23)
    else:
        print("=-" * 18)
        print("O preço unitário é R$ {} \nO valor total a ser pago é: R${}".format(preco, totalNota))
        print("=-" * 18)

elif 10 < codigo <= 20:
    preco = 15.00
    totalNota = preco * qte
    if 250 <= totalNota <= 500:
        desconto = totalNota * 0.1
        precoFinal = totalNota - desconto
        print("=-" * 23)
        print("Preço unitário: R$ {} \nPreço total da nota: R$ {} \nValor do desconto: R$ {} \n"
              "Preço final da nota após o desconto: R$ {} ".format(preco, totalNota, desconto, precoFinal))
        print("=-" * 23)
    else:
        print("=-" * 18)
        print("O preço unitário é R$ {} \nO valor total a ser pago é: R${}".format(preco, totalNota))
        print("=-" * 18)

elif 20 < codigo <= 30:
    preco = 20.00
    totalNota = preco * qte
    if totalNota > 50:
        desconto = totalNota * 0.15
        precoFinal = totalNota - desconto
        print("=-" * 23)
        print("Preço unitário: R$ {} \nPreço total da nota: R$ {} \nValor do desconto: R$ {} \n"
              "Preço final da nota após o desconto: R$ {} ".format(preco, totalNota, desconto, precoFinal))
        print("=-" * 23)
    else:
        print("=-" * 18)
        print("O preço unitário é R$ {} \nO valor total a ser pago é: R${}".format(preco, totalNota))
        print("=-" * 18)

elif 30 < codigo <= 40:
    preco = 30.00
    totalNota = preco * qte
    print("=-" * 18)
    print("O preço unitário é R$ {} \nO valor total a ser pago é: R${}".format(preco, totalNota))
    print("=-" * 18)
