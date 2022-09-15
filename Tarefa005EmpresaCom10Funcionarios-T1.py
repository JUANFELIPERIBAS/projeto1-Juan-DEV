# Algoritimo Tarefa 005: Empresa com 10 funcionários (While)
# Dev: Juan Felipe Ribas
# Data: 29.08.22

"""
10 funcionários
    caracteristicas dos funcionários:
        código;
        número de horas trabalhadas no mês;
        turno de trabalho:
                    M – matutino;
                    V – vespertino;
                    N – noturno.
        categoria:
                    O – operário;
                    G – gerente.

Fazer um programa que:
a) Leia as informações dos funcionários - número de horas trabalhadas - turno de trabalho - categoria
"""

Laco1 = 1
Laco2 = True
Laco3 = True
Laco4 = True

while Laco1 <= 10:
    # Quadro do laço principal
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o código do funcionário: ")

    # ----------------------Condicionais para Hora trabalhada
    while Laco4:
        if HoraTrabalhada = float(input("Digite as horas trabalhadas: ")):
        if HoraTrabalhada = float
            Laco4 = False
        else:
            print("Erro, Digite novamente")
            continue
        break

    #----------------------Condicionais Categoria G e Turno N
    while Laco2:
        Categoria = input("Digite a categoria: ")
        if Categoria == 'O' or Categoria == 'G':
            Laco2 = False
        else:
            print("As categorias possíveis são O e G, digite novamente.")
            continue
        break
    #---------------------Turno M ou V ou N
    while Laco3:
        Turno = input("Digite o Turno: ")
        if Turno == "M" or Turno == 'V' or Turno == 'N':
            Laco3 = False
        else:
            print("Os turnos possiveis são: V ou M ou N, digite novamente.")
            continue
        break
    #----------------------------------------Condicionais para tratar a categoria G e turno N
    if Categoria == "G" and Turno == "N":
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    #---------------------------------------Condicionais para tratar a categoria G e Turno M ou V
    if Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # ---------------------------------------Condicionais para tratar a categoria O e Turno N
    if Categoria == "O" and Turno == "N":
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # ---------------------------------------Condicionais para tratar a categoria O e Turno M ou V
    if Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.10
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    #-------------------------------------Quadro resumo

    print("Código:", Codigo, "Horas trabalhadas:", HoraTrabalhada, "Categoria:", Categoria, "Turno:", Turno)
    print("Valor da hora:", ValorHora, "Salário inicial:", SalarioInicial, "Auxílio alimentação:", AuxilioAlimentacao,
          "Salário final:", SalarioFinal)

    # -------------------------------------Verificar os laços
    print("Número do laço principal:",Laco1)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
print("Fim")






