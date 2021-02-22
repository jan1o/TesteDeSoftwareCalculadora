import unittest
from main import calculadora, calculos, calcAreas

class TestCalculos(unittest.TestCase):

    def test_bhaskara(self):
        delta = calculos.deltaCalc(1, 2, -3)
        resultadoEsperado = [1.0, -3.0]
        self.assertEqual(calculos.bhaskara(1,2,-3, delta), resultadoEsperado)

class TestCalcAreas(unittest.TestCase):
	def test_areaQuadrado(self):
		areaQuadrado = calcAreas.areaQuadrado(10)
		self.assertEqual(areaQuadrado, 100)

	def test_areaRetangulo(self):
		areaRetangulo = calcAreas.areaRetangulo(10, 20)
		self.assertEqual(areaRetangulo, 200)

	def test_areaTriangulo(self):
		areaTriangulo = calcAreas.areaTriangulo(10, 20)
		self.assertEqual(areaTriangulo, 100)
    
if __name__ == '__main__':
    unittest.main()
