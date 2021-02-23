import math
from math import sqrt
from math import pow as pow

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

class calcAreas:
	def areaQuadrado(lado):
		area = calculadora.multiplicacao(lado, lado)
		return area

	def areaRetangulo(base, altura):
		area = calculadora.multiplicacao(base, altura)
		return area

	def areaTriangulo(base, altura):
		area = calculadora.multiplicacao(base, altura)
		area = calculadora.divisao(area, 2)
		return area

class distancia:
    def distanciaPontosReta(x1, y1, x2, y2):
        calc1 = pow(calculadora.subtracao(x2,x1),2)
        calc2 =  pow(calculadora.subtracao(y2,y1),2)
        dist = calculadora.soma(calc1,calc2)
        distAB = sqrt(dist)
        return distAB

    def distanciaPontosEspaco(x1, y1, z1, x2, y2, z2):
        calc1 = pow(calculadora.subtracao(x2,x1),2)
        calc2 = pow(calculadora.subtracao(y2,y1),2)
        calc3 = pow(calculadora.subtracao(z2,z1),2)
        dist = calculadora.soma(calculadora.soma(calc1,calc2),calc3)
        distABC = sqrt(dist)
        return distABC
        

# delta = calculos.deltaCalc(1, 2, -3)   
# print(calculos.bhaskara(1,2,-3, delta))

# A = (-1,-2) e B = (-3,-4)
print(distancia.distanciaPontosReta(-1, -2, -3, -4))
# A = (4, -8, -9) e B = (2, -3, -5).
print(distancia.distanciaPontosEspaco(4, -8, -9, 2, -3, -5))