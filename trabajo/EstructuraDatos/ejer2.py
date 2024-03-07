#•	Crea una clase "Rectángulo" con atributos como longitud y ancho.
# Agrega métodos para calcular el área y el perímetro del rectángulo.
class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)