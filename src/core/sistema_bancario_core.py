class SistemaBancarioCore:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite = 500
        self.limite_saques = 3
        self.numero_saques = 0
        self.extrato_print = ""

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor

            self.extrato.append({
              "tipo": "deposito",
              "valor": valor
            })
            return
        print("Operação falhou! O valor informado é inválido.")

    def saque(self, valor):
        if valor < 0:
            print("Operação falhou! O valor informado é inválido.")
            return

        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return

        if valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return

        if self.saldo >= valor:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato.append({
              "tipo": "saque",
              "valor": valor
            })

    def exibir_extrato(self):
        print("Extrato:")
        for operacao in self.extrato:
            self.extrato_print += f"{operacao['tipo']} de R$ {operacao['valor']:.2f}\n"
        return self.extrato_print
