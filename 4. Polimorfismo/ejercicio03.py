# Clase padre con método abstracto
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def sonido(self):
        pass
    

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def sonido(self):
        print(f"Perro: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}, Sonido: Guau Guau\n")


# Clase hija
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def sonido(self):
        print(f"Gato: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Sonido: Miau Miau\n")


# Clase hija Pájaro
class Pajaro(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie

    def sonido(self):
        print(f"Pájaro: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}, Sonido: Pío Pío\n")


# Creando objetos de las clases hijas
perro1 = Perro("Max", 5, "Labrador")
gato1 = Gato("Luna", 3, "Blanco")
pajaro1 = Pajaro("Tweety", 1, "Canario")

perro1.sonido()
gato1.sonido()
pajaro1.sonido()
