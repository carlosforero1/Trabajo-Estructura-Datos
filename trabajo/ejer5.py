#•	Define un método "saludar()" en la clase "Persona" que muestre un saludo genérico.
# Luego, sobrescribe este método en las clases "Empleado" y "Estudiante"
# para mostrar saludos personalizados.
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

    def saludar(self):
        print(f"¡Hola! Mi nombre es {self.nombre}")

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

    def saludar(self):
        super().saludar()
        print(f"Soy un(a) {self.puesto_trabajo} en esta empresa.")

        class Estudiante(Persona):
            def __init__(self, nombre, edad, genero, grado, escuela):
                super().__init__(nombre, edad, genero)
                self.grado = grado
                self.escuela = escuela

            def get_grado(self):
                return self.grado

            def set_grado(self, nuevo_grado):
                self.grado = nuevo_grado

            def get_escuela(self):
                return self.escuela

            def set_escuela(self, nueva_escuela):
                self.escuela = nueva_escuela

            def saludar(self):
                super().saludar()
                print(f"Estudio en {self.escuela} y estoy en {self.grado}.")

