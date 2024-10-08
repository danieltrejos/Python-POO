# Clase padre con metodo abstracto
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def descripcion(self):
        pass
    

# Clase hija 
class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        print(f"Carro: {self.marca} {self.modelo}, anio: {self.anio}, Número de puertas: {self.num_puertas}\n") 

# Clase hija 
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo  # Tipo de moto

    def descripcion(self):
        print(f"Moto: {self.marca} {self.modelo}, anio: {self.anio}, Tipo: {self.tipo}\n")


# Clase hija 
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_freno):
        super().__init__(marca, modelo, anio)
        self.tipo_freno = tipo_freno  # Tipo de frenos

    def descripcion(self):
        print(f"Bicicleta: {self.marca} {self.modelo}, anio: {self.anio}, Frenos: {self.tipo_freno}\n")



# Creando objetos de las clases hijas
carro1 = Carro("Toyota", "Corolla", 2022, 4)
moto1 = Moto("Yamaha", "YZF-R3", 2021, "Deportiva")
bicicleta1 = Bicicleta("Giant", "Escape 3", 2020, "Frenos de disco")

carro1.descripcion()
moto1.descripcion()
bicicleta1.descripcion()