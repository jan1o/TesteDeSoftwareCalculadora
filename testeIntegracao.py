import unittest
from main import calculadora, calculos

class TestCalculos(unittest.TestCase):

    def test_bhaskara(self):
        delta = calculos.deltaCalc(1, 2, -3)
        resultadoEsperado = [1.0, -3.0]
        self.assertEqual(calculos.bhaskara(1,2,-3, delta), resultadoEsperado)

    
if __name__ == '__main__':
    unittest.main()
