from src.core.sistema_bancario_core import SistemaBancarioCore

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

sistema_bancario = SistemaBancarioCore()

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        sistema_bancario.deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        sistema_bancario.saque(valor)

    elif opcao == "e":
        extrato = sistema_bancario.exibir_extrato()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
