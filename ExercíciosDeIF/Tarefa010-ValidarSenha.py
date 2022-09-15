# 10. Validar senha (IF)

"""
 Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
 A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO
 caso a senha seja válida e  ACESSO NEGADO caso a senha seja inválida.
"""

Senha = int(input("Digite a senha: "))

if Senha != 1234:
    print("Senha incorreta")
else:
    print("Senha correta")