saldo = 520.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 1

while True:
    print("""
    ====== MENU ======
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==================
    """)

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado!")
        else:
            print("Valor inválido.")

    elif opcao == "s":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Valor acima do limite permitido.")
        elif excedeu_saques:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado!")
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n====== EXTRATO ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=====================\n")

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")
