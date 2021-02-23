import math
from math import sqrt
from math import pow as pow


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
    def deltaCalc(a, b, c):
        delta = (b * b) - ((4 * a) * c)
        return delta

    def bhaskara(a, b, c, delta):
        x1 = calculadora.divisao(calculadora.soma(calculadora.multiplicacao(
            b, -1), math.sqrt(delta)), calculadora.multiplicacao(2, a))
        x2 = calculadora.divisao(calculadora.subtracao(calculadora.multiplicacao(
            b, -1), math.sqrt(delta)), calculadora.multiplicacao(2, a))
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
        calc1 = pow(calculadora.subtracao(x2, x1), 2)
        calc2 = pow(calculadora.subtracao(y2, y1), 2)
        dist = calculadora.soma(calc1, calc2)
        distAB = sqrt(dist)
        return distAB

    def distanciaPontosEspaco(x1, y1, z1, x2, y2, z2):
        calc1 = pow(calculadora.subtracao(x2, x1), 2)
        calc2 = pow(calculadora.subtracao(y2, y1), 2)
        calc3 = pow(calculadora.subtracao(z2, z1), 2)
        dist = calculadora.soma(calculadora.soma(calc1, calc2), calc3)
        distABC = sqrt(dist)
        return distABC

#Esse calculo não existe e é apenas uma forma de simular uma integração entre classes e métodos para se testar
class baseIntegracao:
    def quadradoBhaskara(quadrado, x1Bhaskara):
        return quadrado * x1Bhaskara
        
    
