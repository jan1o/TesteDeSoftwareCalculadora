import unittest
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

