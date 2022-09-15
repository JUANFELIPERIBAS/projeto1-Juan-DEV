# uso de biblioteca
import math

print(math.sqrt(100))
print(math.pow(5, 7))
print(2 ** 4)
print(divmod(40, 6))
print(40 // 6)       # DIV
print((40 % 6))      # MOD

# Soma e Subtração ---------------------------------------
print(10 + 2 + 7)

# Potência?????????????????????????? ---------------------------------------
print(2 ^ 4)  # Está errado!!!

# Divisão ---------------------------------------
print(40 / 10)
# print(40 / 0)  # não pode ter divisão por ZERO!!!

# Precedência de operadores ---------------------------------------

# Operadores relacionais ---------------------------------------
# == True, se a e b são iguais
# "==" significa "Exatamente igual" e "=" significa "Atribuição" ou seja, quando for atribuir
# um valor a uma variável, exemplo: X = 10.
print(55 == 55)
# print(55 = 55) apenas um "=" não funciona!!

# != True, se a e b são diferentes ("!=" significa diferente. "<>" não é reconhecido no python).
print(55 != 55)
print(55 != 56)

# Operadores de atribuições ---------------------------------------
# = dado varmem que você quer atribuir um valor

x = 90
print(x)

# incrementar +=
x += 2
print(x)

# Decrementar -=
x -= 10
print(x)

# divisão x 10 /=
x /= 10
print(x)

# div x 10 //=
x = 20
x //= 6
print(x)

# mod x 10 %=
x = 20
x %= 10
print(x)

# Multiplicação x 10 *=
x = 20
x *= 10
print(x)
