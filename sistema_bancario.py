from datetime import datetime


# ---------------- MENU ----------------
def menu_principal():
    return """
============= BANCO PYTHON =============

[1] Criar usuário
[2] Login
[0] Sair

=> """


def menu_conta():
    return """
=========== MENU DA CONTA ===========

[d] Depositar
[s] Sacar
[e] Extrato
[r] Relatório mensal
[q] Logout

=> """


# ---------------- USUÁRIO ----------------
def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")

    if cpf in usuarios:
        print("❌ Usuário já existe.")
        return

    nome = input("Nome completo: ")
    senha = input("Crie uma senha: ")

    usuarios[cpf] = {
        "nome": nome,
        "senha": senha,
        "saldo": 0.0,
        "limite": 500.0,
        "numero_saques": 0,
        "limite_saques": 3,
        "extrato": "",
        "movimentacoes": []
    }

    print("✅ Usuário criado com sucesso!")


def login(usuarios):
    cpf = input("CPF: ")
    senha = input("Senha: ")

    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        print(f"✅ Bem-vinda(o), {usuarios[cpf]['nome']}!")
        return cpf

    print("❌ CPF ou senha inválidos.")
    return None


# ---------------- OPERAÇÕES ----------------
def depositar(usuario):
    try:
        valor = float(input("Valor do depósito: R$ "))

        if valor <= 0:
            print("❌ Valor inválido.")
            return

        usuario["saldo"] += valor
        data = datetime.now()

        usuario["extrato"] += (
            f"[{data.strftime('%d/%m/%Y %H:%M')}] "
            f"Depósito: R$ {valor:.2f}\n"
        )

        usuario["movimentacoes"].append({
            "tipo": "Depósito",
            "valor": valor,
            "data": data
        })

        print("✅ Depósito realizado!")

    except ValueError:
        print("❌ Digite um número válido.")


def sacar(usuario):
    try:
        valor = float(input("Valor do saque: R$ "))

        if valor <= 0:
            print("❌ Valor inválido.")
            return

        if valor > usuario["saldo"]:
            print("❌ Saldo insuficiente.")
            return

        if valor > usuario["limite"]:
            print("❌ Valor excede o limite.")
            return

        if usuario["numero_saques"] >= usuario["limite_saques"]:
            print("❌ Limite de saques atingido.")
            return

        usuario["saldo"] -= valor
        usuario["numero_saques"] += 1
        data = datetime.now()

        usuario["extrato"] += (
            f"[{data.strftime('%d/%m/%Y %H:%M')}] "
            f"Saque: R$ {valor:.2f}\n"
        )

        usuario["movimentacoes"].append({
            "tipo": "Saque",
            "valor": valor,
            "data": data
        })

        print("✅ Saque realizado!")

    except ValueError:
        print("❌ Digite um número válido.")


def mostrar_extrato(usuario):
    print("\n============== EXTRATO ==============")
    print("Nenhuma movimentação." if not usuario["extrato"] else usuario["extrato"])
    print(f"Saldo atual: R$ {usuario['saldo']:.2f}")
    print("=====================================\n")


def relatorio_mensal(usuario):
    try:
        mes = int(input("Mês (1-12): "))
        ano = int(input("Ano (ex: 2025): "))

        total_dep = 0
        total_saq = 0
        qtd = 0

        print("\n========= RELATÓRIO MENSAL =========")

        for mov in usuario["movimentacoes"]:
            if mov["data"].month == mes and mov["data"].year == ano:
                qtd += 1

                if mov["tipo"] == "Depósito":
                    total_dep += mov["valor"]
                else:
                    total_saq += mov["valor"]

                print(
                    f"{mov['data'].strftime('%d/%m/%Y %H:%M')} | "
                    f"{mov['tipo']} | R$ {mov['valor']:.2f}"
                )

        if qtd == 0:
            print("Nenhuma movimentação nesse período.")
        else:
            print("----------------------------------")
            print(f"Total depositado: R$ {total_dep:.2f}")
            print(f"Total sacado:     R$ {total_saq:.2f}")
            print(f"Saldo do mês:     R$ {total_dep - total_saq:.2f}")
            print(f"Operações:       {qtd}")

        print("==================================\n")

    except ValueError:
        print("❌ Mês e ano inválidos.")


# ---------------- SISTEMA ----------------
def sistema_conta(usuario):
    while True:
        opcao = input(menu_conta()).lower()

        if opcao == "d":
            depositar(usuario)

        elif opcao == "s":
            sacar(usuario)

        elif opcao == "e":
            mostrar_extrato(usuario)

        elif opcao == "r":
            relatorio_mensal(usuario)

        elif opcao == "q":
            print("🔒 Logout realizado.")
            break

        else:
            print("❌ Opção inválida.")


def main():
    usuarios = {}

    while True:
        opcao = input(menu_principal())

        if opcao == "1":
            criar_usuario(usuarios)

        elif opcao == "2":
            cpf_logado = login(usuarios)
            if cpf_logado:
                sistema_conta(usuarios[cpf_logado])

        elif opcao == "0":
            print("👋 Sistema encerrado.")
            break

        else:
            print("❌ Opção inválida.")
