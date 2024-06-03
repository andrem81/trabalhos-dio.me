menu = """
===========================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
===========================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe quanto deseja sacar: "))

        sem_limite = valor > limite

        sem_saques = numero_saques >= LIMITE_SAQUES
        
        sem_saldo = valor > saldo
    
        if sem_limite:
            print("ERRoR!O valor excede o limite máximo.")

        elif sem_saques:
            print("ERRoR! Você excedeu o número máximo de saques.")

        elif sem_saldo:
            print("ERRoR! Você não possui saldo suficiente.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("ERRoR! O valor informado é inválido, digite um valor válido.")

    elif opcao == "e":
        print("=========== EXTRATO BANCÁRIO =============")
        print("Nenhuma movimentação realizxada." if not extrato else extrato)
        print(f"Seu saldo é de: R$ {saldo:.2f}")
        print("==================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")