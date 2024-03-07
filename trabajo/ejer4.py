#•	Crea una clase "Estudiante" que herede de la clase "Persona".
#   Agrega atributos como grado y escuela.

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