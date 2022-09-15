# 3. PROVA: Operadores e Expressões em Python
import math

x = 2 + 3 * 5 + 30 // 10

print(x)


# 2 + 3 * 5 + 30 // 10
# 2 + 15 + 30 // 10
# 2 + 15 + 3
# 20

y = 30 // 10
print(y)

z = True or False and not True
print(z)


z = True or False
print(z)

w = not True
print(w)

x = z and w
print("x =: ",x)

#---------------------- ERREI A QUESTÃAAAAAO!!!!!!!!!###-----------------------------------

# O Professor tinha falado para nós sempre imaginarmos "ou" como "+" e "E" como "*"
# "*" tem precedencia em relação ao "+"!!!

#desta forma, o certo é:

# True or False and not True
# 1 + 0 * 0   --------- True sempre vale 1 e False sempre vale 0!!!!
# 1 + 0
# 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

