import math

class main:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 5
        self.d = 10

        soma = calculadora.soma(self.a, self.a)
        subtracao = calculadora.subtracao(self.a, self.a)
        multiplicacao = calculadora.multiplicacao(self.c, self.c)
        divisao = calculadora.divisao(self.d, self.b)

        print("1 + 1 = " , soma)
        print("1 - 1 = " , subtracao)
        print("5 x 5 = " , multiplicacao)
        print("10 / 2 = " , divisao)


class calculadora:
    def soma(a, b):
        resultado = a + b
        return resultado

    def subtracao(a, b):
        resultado = a - b
        return resultado

    def multiplicacao(a, b):
        resultado = a * b
        return resultado

    def divisao(a, b):
        resultado = a / b
        return resultado

class calculos:
    
    def deltaCalc(a, b ,c):
        delta = calculadora.subtracao(calculadora.multiplicacao(b, b), calculadora.multiplicacao(calculadora.multiplicacao(4, a), c))
        return delta
    
    def bhaskara(a, b, c, delta):
        x1 = calculadora.divisao(calculadora.soma(calculadora.multiplicacao(b, -1), math.sqrt(delta)), calculadora.multiplicacao(2, a))
        x2 = calculadora.divisao(calculadora.subtracao(calculadora.multiplicacao(b, -1), math.sqrt(delta)), calculadora.multiplicacao(2, a))
        resultado = [x1, x2]
        return resultado

    
#delta = calculos.deltaCalc(1, 2, -3)   
#print(calculos.bhaskara(1,2,-3, delta))
