

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


