#	Crea una clase "Persona" con atributos como nombre, edad y género.
#	Agrega métodos para obtener y establecer estos atributos.
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


    def saludar(self):
        print("Hola desde persona")

    def getNombre (self):
      return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getGenero (self):
      return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getEdad (self):
      return self.edad

    def setEdad(self, edad):
        self.edad = edad