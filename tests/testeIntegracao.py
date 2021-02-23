import unittest
# from main import calculos, calcAreas, distancia
import main


class TestCalculos(unittest.TestCase):
    def test_bhaskara(self):
        delta = main.calculos.deltaCalc(1, 2, -3)
        resultadoEsperado = [1.0, -3.0]
        self.assertEqual(main.calculos.bhaskara(1, 2, -3, delta), resultadoEsperado)


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

