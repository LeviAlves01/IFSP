class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        import math
        return math.pi + self.raio ** 2
    
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.raio
    
circulo1 = Circulo(10)
circulo2 = Circulo(7)
circulo3 = Circulo(8)

print("====== AREAS ======")
print(f"Area do circulo 1: {round(circulo1.calcular_area(), 2)}")
print(f"Area do circulo 2: {round(circulo2.calcular_area(), 2)}")
print(f"Area do circulo 3: {round(circulo3.calcular_area(), 2)}")

print("\n====== PERIMETROS ======")
print(f"Perimetro do circulo 1: {round(circulo1.calcular_perimetro(), 2)}")
print(f"Perimetro do circulo 2: {round(circulo2.calcular_perimetro(), 2)}")
print(f"Perimetro do circulo 3: {round(circulo3.calcular_perimetro(), 2)}")