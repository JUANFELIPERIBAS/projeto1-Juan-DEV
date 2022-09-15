# Controle de Fluxo de Execução e Funções
# Dev: Juan Felipe Ribas
# Data: 04.09.22

"""
#  Laços for----------------------------------------------------

print("Números em uma lista")
for numero in [1, 1, 2, 3, 5, "gool", 13, "início"]:
    print(numero)

# Percorrendo uma lista de palavras.---------------------------------

print("Palavras em uma lista:")
for palavra in ["Ordem", "e", "Progresso"]:
    print(palavra)

# Percorrendo um intervalo.------------------------------------------

for i in range(10):
    print(i)

for indice, elemento in enumerate(range(-3, 4)):
    print(indice, elemento)


elemento = 10
EstaPresente = False
lista = [1, 2, 7, 10, 15, 20, 50]
for item in lista:
    if item == elemento:
        EstaPresente = True

if EstaPresente:
    print(("Elemento está na lista"))
else:
    print("Elemento não está na lista!")

elemento = 85
lista = [1, 2, 7, 10, 12, 16, 20, 42, 64, 84, 92, 15]
if elemento in lista:
    print("Está na lista!")
else:
    print("Não está na lista!")



# Laços while--------------------------------------------------------

i = 1
while i < 5:
    print(i)
    i = i + 1

n = 7
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
    print(fatorial)
"""
#  Funções em Python----------------------------------------------------

# Exemplo de função que retorna um valor.-------------------------------
"""
def f(n):

    return n

resultado = f(10)
print("O valor do parâmetro é {}".format(resultado))

"""
# Outro exemplo de função que retorna um valor.--------------------------

def eleva_ao_quadrado(n):

    return n ** 2

print("O número {} elevado ao quadrado é {}".format(10, eleva_ao_quadrado(10)))

# Exemplo de função que retorna mais de um valor.-------------------------

def quociente_resto(x, y):

    quociente = x // y

    resto = x % y

    return (quociente, resto)

print("Quociente e resto: ", quociente_resto(9, 4))

#  Funções anônimas (funções lambda)-----------------------------------------

# Função map sem o uso de função lambda: (não deu certo!!)
def eleva_ao_quadrado(n):
    return n ** 2
    print(list(map(eleva_ao_quadrado, range(5))))

# Função map com função lambda.
print(list(map(lambda x: x ** 2, range(5))))


# Função Filter.---------------------------------------------------------
numeros = [1, 2, 3, 4, 5]
output = list(filter(lambda x: x >= 3, numeros))
print(output)