#Implementa una clase "Departamento" que tenga una lista de empleados.
# Decide si la relación entre el departamento y los empleados es de composición o agregación.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

empleado1 = Empleado("geronimo", 50000)
empleado2 = Empleado("carlos", 60000)

departamento = Departamento("Recursos Humanos")
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

for empleado in departamento.empleados:
    print(f"Nombre: {empleado.nombre}, Salario: {empleado.salario}")