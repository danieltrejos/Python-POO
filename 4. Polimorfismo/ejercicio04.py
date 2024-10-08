# Clase padre con método abstracto
class InstrumentoMusical:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    
    def tocar(self):
        pass
    

# Clase hija Guitarra
class Guitarra(InstrumentoMusical):
    def __init__(self, marca, tipo, num_cuerdas):
        super().__init__(marca, tipo)
        self.num_cuerdas = num_cuerdas

    def tocar(self):
        print(f"Guitarra: {self.marca}, Tipo: {self.tipo}, Número de cuerdas: {self.num_cuerdas}, Se toca rasgueando las cuerdas.\n")


# Clase hija Piano
class Piano(InstrumentoMusical):
    def __init__(self, marca, tipo, num_teclas):
        super().__init__(marca, tipo)
        self.num_teclas = num_teclas

    def tocar(self):
        print(f"Piano: {self.marca}, Tipo: {self.tipo}, Número de teclas: {self.num_teclas}, Se toca presionando las teclas.\n")


# Clase hija Trompeta
class Trompeta(InstrumentoMusical):
    def __init__(self, marca, tipo, material):
        super().__init__(marca, tipo)
        self.material = material

    def tocar(self):
        print(f"Trompeta: {self.marca}, Tipo: {self.tipo}, Material: {self.material}, Se toca soplando y presionando los pistones.\n")


# Creando objetos de las clases hijas
guitarra1 = Guitarra("Fender", "Acústica", 6)
piano1 = Piano("Yamaha", "De cola", 88)
trompeta1 = Trompeta("Bach", "De viento", "Latón")

guitarra1.tocar()
piano1.tocar()
trompeta1.tocar()
