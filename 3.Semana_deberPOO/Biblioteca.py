class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int):
        """Modela un libro con título, autor y año de publicación"""
        self.titulo = titulo
        self.autor = autor
        self.anio = anio_publicacion

    def mostrar_info(self) -> str:
        """Devuelve información formateada del libro"""
        return f"'{self.titulo}' por {self.autor} ({self.anio})"


class Biblioteca:
    def __init__(self, nombre: str):
        """Modela una biblioteca con nombre y colección de libros"""
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro: Libro):
        """Añade un libro a la colección"""
        self.libros.append(libro)

    def listar_libros(self):
        """Muestra todos los libros en la biblioteca"""
        print(f"\nLibros en {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.mostrar_info()}")


# Creación de instancias y uso del sistema
if __name__ == "__main__":
    # Crear biblioteca
    biblio_central = Biblioteca("Biblioteca Central")

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Rayuela", "Julio Cortázar", 1963)

    # Agregar libros a la biblioteca
    biblio_central.agregar_libro(libro1)
    biblio_central.agregar_libro(libro2)

    # Mostrar catálogo
    biblio_central.listar_libros()
