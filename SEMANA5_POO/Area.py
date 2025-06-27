"""
Programa básico de estudiante
- Usa tipos de datos: str, int, float, bool
- Sigue convención snake_case
"""

# Crear clase estudiante
class Estudiante:
    def __init__(self, nombre, edad, promedio, beca):
        self.nombre = nombre          # str
        self.edad = edad              # int
        self.promedio = promedio      # float
        self.beca = beca              # bool

# Valores de ejemplo
nombre = "Estefania Ramon"  # str
edad = 18                    # int
promedio = 9.0              # float
beca = True                  # bool

# Crear objeto
alumno = Estudiante(nombre, edad, promedio, beca)

# Mostrar resultados
print("Datos del estudiante:")
print(f"Nombre: {alumno.nombre}")
print(f"Edad: {alumno.edad}")
print(f"Promedio: {alumno.promedio}")
print(f"Beca: {'Sí' if alumno.beca else 'No'}")

# Validación adicional
if alumno.promedio < 6:
    print("Alerta: Promedio bajo")



