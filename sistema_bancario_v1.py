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
extrato = saldo
numeros_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("Deposite o valor desejado: "))
        saldo += deposito
        print(f"Depositado: R$ {deposito}")

    elif opcao == "s":
        print(f"Quantidades de saques diários disponíveis: {LIMITE_SAQUE - numeros_saques}")
        saque = float(input("Saque o valor desejado: "))

        if saque <= saldo and numeros_saques < LIMITE_SAQUE and saque <= limite:
            print(f"Sacado: R$ {saque}")
            saldo -= saque
            numeros_saques += 1
        elif saque > limite:
            print("Valor excedeu o limite por saque!")
        elif numeros_saques >= LIMITE_SAQUE:
            print("Saques diários excedido!")
        else:
            print("Saldo insuficiente!")
                   
    elif opcao == "e":
        print("Exibindo extrato")
        print(f"R$ {saldo}")
    
    elif opcao == "q":
        print("Fechando Sistema Bancário...")
        break
    else:
        print("Operação Inválida, escolher opções disponíveis!")