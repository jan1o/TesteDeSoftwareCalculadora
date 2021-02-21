import unittest
from main import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora.soma(10 , 10), 20)

    def test_subtracao(self):
        self.assertEqual(calculadora.subtracao(10 , 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora.multiplicacao(4 , 3), 12)

    def test_divisao(self):
        self.assertEqual(calculadora.divisao(25 , 5), 5)

if __name__ == '__main__':
    unittest.main()

