# Mentex 4 - Operações com tipos básicos
# Dev: Juan Felipe Ribas
# Data: 03.09.22
"""
x = 1
y = 2

resultado = x + y
print(resultado)
print(type(resultado))  # Mostra qual o tipo da variável resultado.

# ponto flutante (se uma das variáveis for ponto fluante, o resultado sempre vai ser ponto flutuante)
x = 1.5
y = 2.8

resultado = x + y
print(resultado)
print(type(resultado))

# conversão de tipos --- de número inteiro para caracter (ou string)
x = 10
s = str(x)
print(s)
print(type(s))

# conversão de tipos --- de float para inteiro
x = 50.97
b = int(x)
print(b)
print(type(b))

# conversão de tipos --- de inteiro float
x = 60
b = float(x)
print(b)
print(type(b))

# String
StringSemNada = ''
UmaLetra = 'a'
VariasLetras = 'Banana'

print(type(StringSemNada))
print(type(UmaLetra))
print(type(VariasLetras))

# booleanas
"""
a = True
print(type(a))
print(a)
print(not a)
print(not a and False or True)
z = not a and False or True
print(z)
print(z * a)
print(z * a + (a +z))
print(z + a)