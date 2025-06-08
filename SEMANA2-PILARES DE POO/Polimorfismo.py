class Pajaro:
    def volar(self):
        print("El pájaro está volando")

class Avion:
    def volar(self):
        print("El avión está volando")

def que_vuela(obj):
    obj.volar()

pajaro = Pajaro()
avion = Avion()

que_vuela(pajaro)
que_vuela(avion)
