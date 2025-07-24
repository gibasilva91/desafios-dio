menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito = float(input("Valor a depositar: "))
        if valor_deposito <= 0:
            print("O valor de depósito tem que ser maior do que 0")
        else:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso")

    elif opcao == "s":
        print("Saque")

        if numero_de_saques < LIMITE_DE_SAQUES:
            valor_saque = float(input("Valor a ser sacado: "))
            if valor_saque > saldo:
                print("Saque não pode ser realizado pois o valor a ser sacado é maior do que o saldo")
            else:
                if valor_saque > 500:
                    print("Saque não pode ser realizado pois o valor do saque é maior do que o limite de saque")
                else:
                    if valor_saque > 0:
                        saldo -= valor_saque
                        numero_de_saques += 1
                        extrato += f"Saque de R$ {valor_saque:.2f}\n"
                        print("Saque realizado com sucesso")
                    else:
                        print("O valor de saque informado não é válido")
        else:
            print("Saque não pode ser realizado pois já foram feitos os 3 saques diários")
    
    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor selecione novamente uma opção")
