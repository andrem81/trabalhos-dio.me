def menu():
    menu = """ \n
                Menu
    ============================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ============================
    => """
    return input(menu)
 
def func_deposito(saldo, valor, extrato, /):

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def func_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
    return saldo, extrato, numero_saques

def func_extrato(saldo, /, *, extrato):
    print("=========== EXTRATO BANCÁRIO =============")
    print("Nenhuma movimentação realizxada." if not extrato else extrato)
    print(f"Seu saldo é de: R$ {saldo:.2f}")
    print("==================================")




saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()
    

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = func_deposito(saldo, valor, extrato);
    elif opcao == "s":
        saldo, extrato, numero_saques = func_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,)
    elif opcao == "e":
        func_extrato(saldo, extrato=extrato);
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
