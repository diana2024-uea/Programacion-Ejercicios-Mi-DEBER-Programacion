"""
Sistema de Gestión Tecnológica (2025)
Simula el "ingreso" y "salida" de dispositivos usando POO.
"""


class Dispositivo:
    def __init__(self, tipo, marca, modelo):
        """Constructor: registrar dispositivo"""
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        print(f"\n[+] {tipo} ingresado: {marca} {modelo}")

    def __del__(self):
        """Destructor: liberar dispositivo"""
        print(f"\n[-] {self.tipo} retirado: {self.marca} {self.modelo}")


# Registro principal
if __name__ == "__main__":
    print("\nSISTEMA DE INVENTARIO TECH 2025")
    print("--------------------------------")

    # Dispositivos "entran" al sistema
    hp = Dispositivo("Laptop", "HP", "Spectre 12th Gen")
    lg = Dispositivo("Móvil", "LG", "V70 2025")

    # Fin del bloque principal
    print("\nFin del programa. Los dispositivos serán retirados automáticamente.")

"""
OBJETIVO:
---------
1. Demostrar el ciclo de vida de objetos (creación/destrucción)
2. Aplicar constructores/destructores en contexto tecnológico
3. Mostrar mensajes automatizados al gestionar dispositivos

Buenas prácticas implementadas:
- Nombres descriptivos
- Encapsulamiento básico
- Mensajes claros de estado
- Documentación concisa
"""


