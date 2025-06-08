class Animal:
    def hablar(self):
        print("Sonido genérico")

class Perro(Animal):
    def hablar(self):
        print("Guau")

perro = Perro()
perro.hablar()  # Guau
