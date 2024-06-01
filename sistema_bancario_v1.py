menu = """

 ####Conta Bancária####
 #                    #
 #  [d] -> Depositar  #
 #  [s] -> Sacar      #
 #  [e] -> Extrato    #
 #  [q] -> Sair       #
 #                    #
 ######################
    
"""
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("Deposite o valor desejado: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depositado: R$ {deposito:.2f}")

        else:
            print("Valor inválido para depósito!")

    elif opcao == "s":

        print(f"Quantidade de saques diários disponíveis: {LIMITE_SAQUE - numeros_saques}")
        saque = float(input("Saque o valor desejado: "))

        if saque > 0 and saque <= saldo and numeros_saques < LIMITE_SAQUE and saque <= limite:
            print(f"Sacado: R$ {saque:.2f}")
            saldo -= saque
            numeros_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"

        elif saque > limite:
            print("Valor excedeu o limite por saque!")

        elif numeros_saques >= LIMITE_SAQUE:
            print("Saques diários excedido!")

        elif saque < 0:
            print("Valor informado Inválido!")

        else:
            print("Saldo insuficiente!")
                   
    elif opcao == "e":
        print("\n__________ Extrato __________")

        if not extrato:
            print("Sem movimentação")
        
        else: 
            print(extrato)

        print("-----------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-----------------------------")
        print("_____________________________")

    elif opcao == "q":
        print("Fechando Sistema Bancário...")
        break

    else:
        print("Operação Inválida, escolher opções disponíveis!")