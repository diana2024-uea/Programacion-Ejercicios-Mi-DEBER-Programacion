import os
import subprocess


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/c', 'start', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    # Define la ruta base para el proyecto de Estefanía.
    # AHORA ESTA RUTA ES LA CARPETA 'ESTEFANIA_SEMESTRES2_PARALELOA_POO'
    # Basado en tu explicación: C:\Users\milen\PycharmProjects\ESTEFANIA_SEMESTRES2_PARALELOA_POO
    ruta_base_proyecto = r"C:\Users\milen\PycharmProjects\ESTEFANIA_SEMESTRES2_PARALELOA_POO"  # <--- ¡RUTA AJUSTADA!

    # Define las "unidades" (carpetas de las semanas) manualmente,
    # con los nombres exactos que se ven en tu explorador de PyCharm.
    unidades_semanas = {
        "1": "1.Semana_deberPOO",
        "2": "2.Semana_deberPOO",
        "3": "3.Semana_deberPOO",
        "4": "4.Semana_deberPOO",
        "5": "5.Semana_deberPOO"
    }

    while True:
        print("\nMenú Principal - Navegación por Semanas")
        for key, value in unidades_semanas.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion_semana_str = input("Elige una semana (por su número) o '0' para salir: ")

        if eleccion_semana_str == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_semana_str in unidades_semanas:
            nombre_carpeta_semana = unidades_semanas[eleccion_semana_str]
            ruta_carpeta_semana = os.path.join(ruta_base_proyecto, nombre_carpeta_semana)

            if os.path.isdir(ruta_carpeta_semana):
                # Si la carpeta de la semana existe, muestra los scripts dentro de ella.
                mostrar_scripts(ruta_carpeta_semana)
            else:
                print(
                    f"Error: La carpeta '{nombre_carpeta_semana}' no se encontró en la ruta base '{ruta_base_proyecto}'.")
                print("Por favor, verifica la ruta de tu proyecto en el script 'dashboard.py'.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_scripts(ruta_sub_carpeta):
    # Filtra solo los archivos .py en la carpeta actual
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    if not scripts:
        print(f"No se encontraron scripts Python (.py) en '{ruta_sub_carpeta}'.")
        return

    while True:
        print(f"\nScripts en {os.path.basename(ruta_sub_carpeta)} - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al menú principal")

        eleccion_script = input("Elige un script o '0' para regresar al menú principal: ")
        if eleccion_script == '0':
            break  # Regresa al menú de semanas
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()