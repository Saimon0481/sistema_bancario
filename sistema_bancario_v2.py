def depositar(deposito, saldo, extrato):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Depositado: R$ {deposito:.2f}")
    else:
        print("Valor inválido para depósito!")

    return saldo, extrato

def sacar(*,saque, numeros_saques, limite_saques, limite, saldo, extrato):
    if saque > 0 and saque <= saldo and numeros_saques < limite_saques and saque <= limite:
        print(f"Sacado: R$ {saque:.2f}")
        saldo -= saque
        numeros_saques += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
    
    elif saque > limite:
        print("Valor excedeu o limite por saque!")

    elif numeros_saques >= limite_saques:
        print("Saques diários excedido!")

    elif saque < 0:
        print("Valor informado Inválido!")

    else:
        print("Saldo insuficiente!")
    
    return numeros_saques, saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n__________ Extrato __________")

    if not extrato:
        print("Sem movimentação")
        
    else: 
        print(extrato)

        print("-" * 29)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-" * 29)
        print("_" * 29)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado em nosso banco de dados!")
        return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF (somente números): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "nome": usuario['nome'], "cpf": cpf})
            print("Conta criada com sucesso!")
            return
    print("Usuário não encontrado em nosso banco de dados!")

def info_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            cliente = f"""
    Informação do cliente abaixo:
                
    Nome: {usuario["nome"]}
    CPF: {usuario["cpf"]}
    Data de Nascimento: {usuario["data_nascimento"]}
    Endereço: {usuario["endereco"]}
    """
            print(cliente)
            return
    print("Usuário não encontrado em nosso banco de dados!")

def info_contas(usuarios, contas):
    cpf = input("Informe o CPF (somente números): ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(f"Contas do cliente {usuario['nome']}:")
            for conta in contas:
                if conta['cpf'] == cpf:
                    dados_conta = f"""
    Informação da(s) conta(s) do cliente:
                
    Nome: {conta["nome"]}
    CPF: {conta["cpf"]}
    Agência: {conta["agencia"]}
    Conta: {conta["numero_conta"]}
    """
                    print(dados_conta)
            return
    print("Usuário não encontrado em nosso banco de dados!")
   
def main():

    menu = """

    #########Conta Bancária#########
    #                              #
    #  [d]  -> Depositar           #
    #  [s]  -> Sacar               #
    #  [e]  -> Extrato             #
    #  [nu] -> Novo usuário        #
    #  [nc] -> Nova conta          #
    #  [iu] -> Info do Usuário     #
    #  [ic] -> Info da(s) Conta(s) #
    #  [q] -> Sair                 #
    #                              #
    ################################
    
    """
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []


    while True:
        opcao = input(menu)

        if opcao == "d":
            deposito = float(input("Deposite o valor desejado: "))

            saldo, extrato = depositar(deposito, saldo, extrato)

        elif opcao == "s":
            print(f"Quantidade de saques diários disponíveis: {LIMITE_SAQUE - numeros_saques}")
            print("Valor do saque não deve ultrapassar R$ 500,00")
            valor = float(input("Informe o valor do saque: "))

            numeros_saques, saldo, extrato = sacar(
                saldo=saldo,
                saque=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "iu":
            info_usuario(usuarios)    

        elif opcao == "ic":
            info_contas(usuarios, contas)

        elif opcao == "q":
            break

        else:
            print("Entrada inválida, selecione opção válida!")


main()