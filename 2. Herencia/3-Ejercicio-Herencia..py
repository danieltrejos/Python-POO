class Instrumento:
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = float(input("Ingrese el precio del instrumento: "))

    def registrar(self):
        print("--------------------------")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio: ${self.precio}")
        

class Guitarra(Instrumento):
    def __init__(self, tipo, marca, material, num_cuerdas):
        super().__init__(tipo, marca, material)
        self.num_cuerdas = num_cuerdas
        self.acordes = input("Ingrese los acordes básicos que conoce (separados por comas): ").split(',')

    def registrar(self):
        super().registrar()
        print(f"Número de cuerdas: {self.num_cuerdas}")
        print("--------------------------")
    
    def tocar(self):
        print("Tocando la guitarra...")
        for acorde in self.acordes:
            print(f"Tocando el acorde {acorde}")

# Instancia de Guitarra
guitarra1 = Guitarra("Guitarra Acústica", "Fender", "Madera", 6)
# Registrar detalles guitarra
guitarra1.registrar()
# Tocar la guitarra
guitarra1.tocar()