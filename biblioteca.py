class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int):
        """Modela un libro con título, autor y año de publicación"""
        self.titulo = titulo
        self.autor = autor
        self.anio = anio_publicacion

    def mostrar_info(self) -> str:
        """Devuelve información formateada del libro"""
        return f"'{self.titulo}' por {self.autor} ({self.anio})"
