class Vehiculo:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.numero_llantas = int(input("No. de Llantas: "))

    def registrar(self):
        print("-----")
        print("CARRO REGISTRADO")
        print("-----")
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("Modelo: ", self.modelo)
        print("No. de Llantas: ", self.numero_llantas)

class Carro(Vehiculo):
    def __init__(self, marca, color, modelo, placa):
        super().__init__(marca, color, modelo)
        self.placa = placa
        self.gasolina = int(input("No. de Galones de Gasolina: "))

    def encender(self):
        print("Placa: ", self.placa)
        if self.gasolina > 0:
            print("-----------------")
            print(f"El carro {self.marca}, con placa {self.placa} de color {self.color} enciende !!")
        else:
            print("-----------------")
            print(f"El carro {self.marca}, con placa {self.placa} de color {self.color} no enciende !!")

# Instanciando la subclase Carro
objeto_carro = Carro('SUZUKI', 'Rojo', '2022', 'PPC 54C')

objeto_carro.registrar()  # Registrando el carro
objeto_carro.encender()   # Encendiendo el carro