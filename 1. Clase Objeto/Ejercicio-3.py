class Carro:
    # Creo el constructor de la clase
    def __init__(self, marca, modelo, año, color, combustible):
        # Defino los atributos de la instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.combustible = combustible
    # Muestro los detalles de los objetos
    def mostrar_detalles(self):
        print("Mostrar detalles del objeto")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Combustible: {self.combustible}")
        print ("------------------------------------------------------")
    # Metodos de la clase
    def arrancar(self):
        print(f"El Carro: {self.marca} {self.modelo} arrancó...")
    def detener(self):
        print(f"El Carro: {self.marca} {self.modelo} se detuvo...")
        
    
    
# Creo una instancia de la clase Carro
carro1 = Carro ("Toyota", "Hilux","2000","Gris", "Diesel")
carro2 = Carro ("Mazda", "Cx-30","2024","Rojo", "Gasolina")
carro3 = Carro ("Susuki", "Sj","1986","Negro", "Gasolina")

# mostrar_detalles

carro1.mostrar_detalles()
carro2.mostrar_detalles()
carro3.mostrar_detalles()

# usando metodos

carro1.arrancar()
carro1.detener()

