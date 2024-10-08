class Reloj:
    def __init__(self, marca, tipo, material):
        self.marca = marca
        self.tipo = tipo
        self.material = material
        self.precio = float(input("Ingrese el precio del reloj: "))

    def registrar(self):
        print("------------------------")
        print("Detalles del reloj:")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio: ${self.precio}\n")

class RelojInteligente(Reloj):
    def __init__(self, marca, tipo, material, pantalla, sistema_operativo):
        super().__init__(marca, tipo, material)
        self.pantalla = pantalla
        self.sistema_operativo = sistema_operativo

    def registrar(self):
        super().registrar()
        print(f"Pantalla: {self.pantalla}")
        print(f"Sistema operativo: {self.sistema_operativo}\n")

    def encender(self):
        self.nivel_bateria = int(input("Ingresar el (nivel) % de bateria del laptop: "))
        if self.nivel_bateria >= 0 and self.nivel_bateria <= 100:
            print("\nEncendiendo el reloj inteligente...")
            print("\nMostrando detalles...")
            self.registrar()
        else:
            print("\nNivel de bateria incorrecto no se puede encender el dispositivo.")
        

# Instancia RelojInteligente
mi_reloj = RelojInteligente("Apple", "Deportivo", "Aluminio", "OLED", "watchOS")

# Registrar los detalles
mi_reloj.registrar()
# Encender
mi_reloj.encender()