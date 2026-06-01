import unittest
from logistica_erp import calcular_frete

class TestLogisticaERP(unittest.TestCase):

    def test_distancia_invalida(self):
        with self.assertRaises(ValueError):
            calcular_frete(0, 10, False)

    def test_peso_invalido(self):
        with self.assertRaises(ValueError):
            calcular_frete(100, -5, False)

    def test_frete_minimo_normal(self):
        # dist <= 100 (150), peso <= 5 (100) = 250
        self.assertEqual(calcular_frete(50, 4, False), 250)

    def test_frete_medio_acrescimo_distancia(self):
        # dist <= 500 (300), peso <= 20 (300) = 600
        # dist > 300 and peso > 10 (+200) = 800
        self.assertEqual(calcular_frete(400, 15, False), 800)

    def test_frete_maximo_carga_perigosa(self):
        # dist > 500 (500), peso > 20 (600) = 1100
        # perigosa (* 1.5) = 1650
        # perigosa (+200) = 1850
        self.assertEqual(calcular_frete(600, 25, True), 1850)

    def test_frete_excecao_curta_pesada(self):
        # dist < 50 and peso > 30 = retorna -1
        self.assertEqual(calcular_frete(30, 40, False), -1)

if __name__ == '__main__':
    unittest.main()
