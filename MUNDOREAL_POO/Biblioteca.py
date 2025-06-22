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
