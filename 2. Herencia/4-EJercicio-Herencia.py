class Electronico:
    def __init__(self, marca, modelo, procesador):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = int(input("Ingrese la cantidad de RAM en GB: "))

    def registrar(self):
        print("Detalles del dispositivo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")

class Laptop(Electronico):
    def __init__(self, marca, modelo, procesador, disco_duro):
        super().__init__(marca, modelo, procesador)
        self.disco_duro = disco_duro
        self.bateria = int(input("Ingrese la duración de la batería en horas: "))

    def registrar(self): # Polimorfismo para mejorar el metodo de registrar
        super().registrar()
        print(f"Disco duro: {self.disco_duro}")
        print(f"Duración de la batería: {self.bateria} horas")
    
    def encender(self):
        self.nivel_bateria = int(input("Ingresar el (nivel) % de bateria del laptop: "))
        if self.nivel_bateria >= 0 and self.nivel_bateria <= 100:
            print("\nEncendiendo la laptop...")
            print("\nMostrando detalles...")
            self.registrar()
        else:
            print("\nLa batería no puede tener un nivel menor o igual a 0 ni mayor o igual a 100% para encender.")

# Crear una instancia de la clase Laptop
laptop1 = Laptop("Dell", "XPS 13", "Intel Core i7", "SSD 512GB")
laptop1.registrar()
laptop1.encender()