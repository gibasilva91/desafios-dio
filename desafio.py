saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
clientes = []
contas = []
sequencia_conta = 1
NUMERO_DA_AGENCIA = "0001"

def menu():
    opcao = input(
    """
    [c] - Cadastrar cliente
    [l] - Listar clientes
    [cc] - Criar conta
    [lc] - Listar contas
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
    => """)

    return opcao

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > saldo:
            print("Saque não pode ser realizado pois o valor a ser sacado é maior do que o saldo")
        else:
            if valor > limite:
                print("Saque não pode ser realizado pois o valor do saque é maior do que o limite de saque")
            else:
                if valor > 0:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque de R$ {valor:.2f}\n"
                    print("Saque realizado com sucesso")
                else:
                    print("O valor de saque informado não é válido")
    else:
        print("Saque não pode ser realizado pois já foram feitos os 3 saques diários")

    return saldo, extrato

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("O valor de depósito tem que ser maior do que 0")
    else:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso")

    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("Extrato")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}\n")

def criar_cliente(nome, data_de_nascimento, cpf, endereco):

    cliente = {"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco}

    cliente_ja_existe = 0

    for cliente_existente in clientes:
        if cliente_existente['cpf'] == cpf:
            cliente_ja_existe += 1
            break
    
    if cliente_ja_existe == 1:
        print("Já existe um cliente cadastrado com esse CPF.")
    else:
        print("Cliente criado com sucesso")
        return clientes.append(cliente)

def criar_conta(agencia, numero_da_conta, cpf_do_cliente):
    
    global sequencia_conta

    conta = {"agencia": agencia, "numero_da_conta": numero_da_conta, "cpf_do_cliente": cpf_do_cliente}

    cpf_ja_existe = 0

    for cpf_existente in clientes:
        if cpf_existente['cpf'] == cpf_do_cliente:
            cpf_ja_existe += 1
            break

    if cpf_ja_existe == 1:  
        sequencia_conta += 1
        print("Conta criada com sucesso")
        return contas.append(conta)
    else:
        print("Não existe nenhum cliente para o CPF informado")

def main():

    while True:
        
        opcao = menu()

        if opcao == "c":
            nome = input("Nome do cliente: ")
            data_de_nascimento = input("Data de nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")

            criar_cliente(nome, data_de_nascimento, cpf, endereco)
        
        elif opcao == "l":
            if not clientes:
                print("Ainda não existem clientes cadastrados")
            else:
                for cliente in clientes:
                    print(cliente)

        elif opcao == "cc":
            cpf = input("Digite o CPF do cliente o qual deseja criar a conta: ")
            criar_conta(NUMERO_DA_AGENCIA, sequencia_conta, cpf)

        elif opcao == "lc":
            if not contas:
                print("Ainda não existem contas cadastradas")
            else:
                for conta in contas:
                    print(conta)

        elif opcao == "d":
            valor_deposito = float(input("Valor a depositar: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor = float(input("Valor a ser sacado: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_de_saques, limite_saques=LIMITE_DE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida. Por favor selecione novamente uma opção")

main()
