import unittest
from main import calculadora, calculos, distancia

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(10 , 10), 20)

    def test_subtracao(self):
        self.assertEqual(calculadora.subtracao(10 , 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora.multiplicacao(4 , 3), 12)

    def test_divisao(self):
        self.assertEqual(calculadora.divisao(25 , 5), 5)
        
class TestCalculos(unittest.TestCase):

    def test_deltaCalc(self):
        self.assertEqual(calculos.deltaCalc(1 ,2, -3), 16)

class TestDistancia(unittest.TestCase):

    def test_distReta(self):
        self.assertEqual(distancia.distanciaPontosReta(-1, -2, -3, -4), 2.8284271247461903)
        
    def test_distEspaco(self):
        self.assertEqual(distancia.distanciaPontosEspaco(4, -8, -9, 2, -3, -5), 6.708203932499369)

    
if __name__ == '__main__':
    unittest.main()

