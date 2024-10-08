"""
Ejercicio 2: Clase Producto
Crea una clase Producto que tenga los siguientes atributos privados: nombre, precio. 
La clase también debe incluir los atributos públicos, cantidad, categoría. 
Implementa métodos getter y setter para cada atributo privado. 
Además, crea un método que muestre toda la información del producto.
"""
class Producto:
    def __init__(self, nombre, precio,cantidad, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoria : {self.categoria}")
    
    #getters
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_precio(self):
        return self.__precio
    
    #setters
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    

# objeto    
producto = Producto("Tenis", 100000, 10, "Deportivos")    

producto.mostrar_informacion()

print("------------------------------------")


producto.establecer_nombre("Zapatos")
producto.establecer_precio(105000)

print(f"Nombres: {producto.obtener_nombre()}")
print(f"Precio: {producto.obtener_precio()}")
print(f"Cantidad: {producto.cantidad}")
print(f"Categoria: {producto.categoria}")