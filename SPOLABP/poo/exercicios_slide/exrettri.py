from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        import math
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
ret1 = Retangulo(5, 10)
ret2 = Retangulo (8, 20)
tri1 = Triangulo(10, 9, 8)
tri2 = Triangulo(15, 14, 13)

formas = [ret1, ret2, tri1, tri2]
for forma in formas:
    print("Área:", forma.calcular_area())
    print("Perímetro:", forma.calcular_perimetro())
    print("---")
