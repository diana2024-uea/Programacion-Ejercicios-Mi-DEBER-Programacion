class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # privado

    def mostrar_edad(self):
        print(f"{self.nombre} tiene {self.__edad} años")

persona = Persona("Luis", 30)
persona.mostrar_edad()
# print(persona.__edad)  # Error, atributo privado


