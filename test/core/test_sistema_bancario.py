import unittest

from core.sistema_bancario_core import SistemaBancarioCore


class TestSistemaBancario(unittest.TestCase):
    def test_deposito_positivo(self):
        sistema = SistemaBancarioCore()
        sistema.deposito(100)
        self.assertEqual(sistema.saldo, 100)

    def test_deposito_negativo(self):
        sistema = SistemaBancarioCore()
        sistema.deposito(-100)
        self.assertEqual(sistema.saldo, 0)

    def test_saque_positivo(self):
        sistema = SistemaBancarioCore()
        sistema.deposito(100)
        sistema.saque(50)
        self.assertEqual(sistema.saldo, 50)

    def test_saque_negativo(self):
        sistema = SistemaBancarioCore()
        sistema.deposito(100)
        sistema.saque(-50)
        self.assertEqual(sistema.saldo, 100)


if __name__ == "__main__":
    unittest.main()
