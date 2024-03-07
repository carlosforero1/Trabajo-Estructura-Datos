#Crea una clase "Empleado" que herede de la clase "Persona".
# Agrega atributos adicionales como salario y puesto de trabajo.

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    def get_genero(self):
        return self.genero

    def set_genero(self, nuevo_genero):
        self.genero = nuevo_genero

        class Empleado(Persona):
            def __init__(self, nombre, edad, genero, salario, puesto_trabajo):
                super().__init__(nombre, edad, genero)
                self.salario = salario
                self.puesto_trabajo = puesto_trabajo

            def get_salario(self):
                return self.salario

            def set_salario(self, nuevo_salario):
                self.salario = nuevo_salario

            def get_puesto_trabajo(self):
                return self.puesto_trabajo

            def set_puesto_trabajo(self, nuevo_puesto_trabajo):
                self.puesto_trabajo = nuevo_puesto_trabajo