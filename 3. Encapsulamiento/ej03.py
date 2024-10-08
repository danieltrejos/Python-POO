class Libro:
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.editorial = editorial

    def mostrar_informacion(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

    # Getters
    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def obtener_isbn(self):
        return self.__isbn

    # Setters
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn


# Objeto de la clase Libro
libro = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0", "Editorial Clásica")

# Mostrar la información del libro
libro.mostrar_informacion()

print("------------------------------------")

# Modificar los atributos privados usando los setters
libro.establecer_titulo("Don Quijote de la Mancha")
libro.establecer_autor("Miguel de Cervantes Saavedra")
libro.establecer_isbn("978-84-376-0494-7")

# Mostrar la nueva información del libro
print(f"Título: {libro.obtener_titulo()}")
print(f"Autor: {libro.obtener_autor()}")
print(f"ISBN: {libro.obtener_isbn()}")
print(f"Editorial: {libro.editorial}")
