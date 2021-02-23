import unittest
from unittest.mock import MagicMock
import main


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(main.calculadora.soma(10, 10), 20)

    def test_subtracao(self):
        self.assertEqual(main.calculadora.subtracao(10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(main.calculadora.multiplicacao(4, 3), 12)

    def test_divisao(self):
        self.assertEqual(main.calculadora.divisao(25, 5), 5)


class TestCalculos(unittest.TestCase):

    def test_deltaCalc(self):
        self.assertEqual(main.calculos.deltaCalc(1, 2, -3), 16)

    def test_bhaskara(self):
        calc = main.calculos()
        calc.deltaCalc = MagicMock(return_value=16)
        delta = calc.deltaCalc(1, 2, -3)
        self.assertEqual(main.calculos.bhaskara(1, 2, -3, delta), [1, -3])

class TestCalcAreas(unittest.TestCase):
    def test_areaQuadrado(self):
        areaQuadrado = main.calcAreas.areaQuadrado(10)
        self.assertEqual(areaQuadrado, 100)

    def test_areaRetangulo(self):
        areaRetangulo = main.calcAreas.areaRetangulo(10, 20)
        self.assertEqual(areaRetangulo, 200)

    def test_areaTriangulo(self):
        areaTriangulo = main.calcAreas.areaTriangulo(10, 20)
        self.assertEqual(areaTriangulo, 100)


class TestDistancia(unittest.TestCase):
    def test_distReta(self):
        self.assertEqual(main.distancia.distanciaPontosReta(-1, -2, -3, -4), 2.8284271247461903)

    def test_distEspaco(self):
        self.assertEqual(main.distancia.distanciaPontosEspaco(4, -8, -9, 2, -3, -5), 6.708203932499369)

