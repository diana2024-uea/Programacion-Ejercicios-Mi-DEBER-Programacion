class ClimaDiario:
    def __init__(self):
        # Encapsula la lista de temperaturas dentro del objeto
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        # Método para agregar una temperatura a la lista interna
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        # Calcula el promedio de las temperaturas almacenadas
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

clima = ClimaDiario()

print("Ingrese las temperaturas diarias para una semana:")

for dia in range(1, 8):
    while True:
        entrada = input(f"Día {dia}: ")
        try:
            temp = float(entrada)  # Validación para asegurar que la entrada es numérica
            clima.ingresar_temperatura(temp)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

promedio = clima.calcular_promedio_semanal()
# Mostrar el promedio con tres decimales
print("Promedio semanal (POO): {:.2f}".format(promedio))


