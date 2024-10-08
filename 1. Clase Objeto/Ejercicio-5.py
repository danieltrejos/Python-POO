# Defino la clase
class Figura_geometrica:
    # Defino el constuctor
    def __init__(self, nombre, lados, perimetro, area, color):
        # Defino los atributos de la instancia de la clase
        self.nombre = nombre
        self.lados = lados
        self.perimetro = perimetro
        self.area = area
        self.color = color
    # Defino metodos para mostrar los atributos de los objetos de la clase
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Lados: {self.lados}")
        print(f"Perimetro: {self.perimetro}")
        print(f"Area: {self.area}")
        print(f"Color: {self.color}")
        print ("------------------------------------------------------")
    def calcular_perimetro(self):
        print(f"El Perimetro del: {self.nombre} es {self.perimetro}")
    def calcular_area(self):
        print(f"El area del: {self.nombre} es {self.area}")
# Creo objetos de la clase
figura1 = Figura_geometrica("Triangulo", "3","10mt","20mt2","Rojo")
figura2 = Figura_geometrica("Cuadrado","4","20mt", "25mt2","Azul")
figura3 = Figura_geometrica("Trapecio","4","20mt","25mt2", "Naranja")

# Mostrar detalles de los objetos

figura1.mostrar_detalles()
figura2.mostrar_detalles()
figura3.mostrar_detalles()

# Usar metodos

figura1.calcular_perimetro()
figura1.calcular_area()

figura2.calcular_perimetro()
figura2.calcular_area()