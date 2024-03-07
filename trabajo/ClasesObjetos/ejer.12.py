#Agrega un método estático en la clase "Empleado"
# que calcule el salario promedio de todos los empleados creados
class Empleado:
    empleados = []  # Lista para realizar un seguimiento de todos los empleados creados

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.empleados.append(self)  # Agrega la instancia actual a la lista de empleados

    @staticmethod
    def salario_promedio():
        if not Empleado.empleados:
            return 0
        total_salarios = sum(empleado.salario for empleado in Empleado.empleados)
        return total_salarios / len(Empleado.empleados)

# Ejemplo de uso:
empleado1 = Empleado("Juan", 50000)
empleado2 = Empleado("Maria", 60000)

print(f"Salario promedio de todos los empleados: {Empleado.salario_promedio()}")