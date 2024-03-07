#Define una clase "Motor" y una clase "Coche". El coche debe tener un motor.
# Decide si la relación entre el coche y el motor es de composición o agregación y
# diseña las clases en consecuencia.
class Motor:
    def __init__(self, tipo, cilindros):
        self.tipo = tipo
        self.cilindros = cilindros

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo="Gasolina", cilindros=4)

# Ejemplo de uso:
mi_coche = Coche(marca="Toyota", modelo="Corolla")
print(f"Marca: {mi_coche.marca}, Modelo: {mi_coche.modelo}")
print(f"Motor: Tipo - {mi_coche.motor.tipo}, Cilindros - {mi_coche.motor.cilindros}")