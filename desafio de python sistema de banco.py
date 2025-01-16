def menu():
    menu_text = """ 
                Menu
    ============================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ============================
    => """
    return input(menu_text)

def deposit(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def withdraw(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("Error! O valor excede o limite máximo.")
    elif numero_saques >= limite_saques:
        print("Error! Você excedeu o número máximo de saques.")
    elif valor > saldo:
        print("Error! Você não possui saldo suficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Error! O valor informado é inválido, digite um valor válido.")
    return saldo, extrato, numero_saques

def print_statement(saldo, extrato):
    print("=========== EXTRATO BANCÁRIO =============")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"Seu saldo é de: R$ {saldo:.2f}")
    print("==========================================")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposit(saldo, valor, extrato)
    elif opcao == "s":
        valor = float(input("Informe quanto deseja sacar: "))
        saldo, extrato, numero_saques = withdraw(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
    elif opcao == "e":
        print_statement(saldo, extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
