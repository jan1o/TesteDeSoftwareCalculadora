import unittest
import main


class TestCalculos(unittest.TestCase):
    def test_bhaskara(self):
        delta = main.calculos.deltaCalc(1, 2, -3)
        resultadoEsperado = [1.0, -3.0]
        self.assertEqual(main.calculos.bhaskara(1, 2, -3, delta), resultadoEsperado)

class TestBaseIntegracao(unittest.TestCase):
    def test_quadradoBhaskara(self):
        quadrado = main.calcAreas.areaQuadrado(5)
        delta = main.calculos.deltaCalc(1, 2, -3)
        bhaskara = main.calculos.bhaskara(1, 2, -3, delta)
        x1Bhaskara = bhaskara[0]
        self.assertEqual(main.baseIntegracao.quadradoBhaskara(quadrado,x1Bhaskara), 25) 



