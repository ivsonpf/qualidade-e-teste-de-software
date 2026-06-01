import unittest
from modulo_seguro import calcular_seguro_carga

class TestModuloSeguroCarga(unittest.TestCase):
    
    def test_caminho_dados_invalidos(self):
        # Garante que o sistema barra entradas corrompidas lançando exceção
        with self.assertRaises(ValueError):
            calcular_seguro_carga(-500, 100, False)
            
    def test_caminho_altissimo_risco(self):
        # Valor > 100k e Carga Perigosa (Taxa 8%)
        resultado = calcular_seguro_carga(150000.0, 600, True)
        self.assertEqual(resultado, 12000.0)

    def test_caminho_alto_valor_estavel(self):
        # Valor > 100k e Carga Normal (Taxa 5%)
        resultado = calcular_seguro_carga(150000.0, 600, False)
        self.assertEqual(resultado, 7500.0)

    def test_caminho_medio_valor_longa_distancia(self):
        # Valor > 20k, Dist > 500, Carga Normal (Taxa 4%)
        resultado = calcular_seguro_carga(50000.0, 600, False)
        self.assertEqual(resultado, 2000.0)

    def test_caminho_medio_valor_curta_distancia(self):
        # Valor > 20k, Dist <= 500, Carga Normal (Taxa 3%)
        resultado = calcular_seguro_carga(50000.0, 100, False)
        self.assertEqual(resultado, 1500.0)

    def test_caminho_regra_salvaguarda(self):
        # Valor <= 100k e Carga Perigosa (+1% na base)
        # Ex: Valor > 20k, dist <= 500 (Base 3%) + Perigosa (1%) = 4%
        resultado = calcular_seguro_carga(50000.0, 100, True)
        self.assertEqual(resultado, 2000.0)

    def test_caminho_baixo_valor_normal(self):
        # Valor <= 20k, Carga Normal (Taxa 2%)
        resultado = calcular_seguro_carga(10000.0, 100, False)
        self.assertEqual(resultado, 200.0)

if __name__ == '__main__':
    unittest.main()
