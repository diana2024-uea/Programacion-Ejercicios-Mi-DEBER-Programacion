# Lista global para almacenar temperaturas semanales
temperaturas_semanales = []

def ingresar_temperatura(temperatura):
    # Agrega la temperatura ingresada a la lista global
    global temperaturas_semanales
    temperaturas_semanales.append(temperatura)

def calcular_promedio_semanal():
    # Calcula el promedio de las temperaturas almacenadas
    global temperaturas_semanales
    if len(temperaturas_semanales) == 0:
        return 0
    return sum(temperaturas_semanales) / len(temperaturas_semanales)

print("Ingrese las temperaturas diarias para una semana:")

for dia in range(1, 8):
    while True:
        entrada = input(f"Día {dia}: ")
        try:
            temp = float(entrada)  # Validación para asegurar que la entrada es numérica
            ingresar_temperatura(temp)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

promedio = calcular_promedio_semanal()
# Mostrar el promedio con tres decimales
print("Promedio semanal (Tradicional): {:.2f}".format(promedio))

