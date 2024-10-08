# Defino la clase
class  Moto:
    # Defino el metodo contructor de clase
    def __init__(self, marca, modelo, año, color, tipo_carroceria):
        # Defino los atributo de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_carroceria = tipo_carroceria
    # Defino metodo para mostrar el estado de las instanscias
    def mostrar_detalles(self):
        print ("Mostrar atributos del objeto")
        print (f"Marca: {self.marca}")
        print (f"Modelo: {self.modelo}")
        print (f"Año: {self.año}")
        print (f"Color: {self.color}")
        print (f"Tipo de carroceria: {self.tipo_carroceria}")
        print ("------------------------------------------------------")
    # Metodos de clase
    def encender(self):
        print (f"La Moto: {self.marca} {self.modelo} encendio a 100km/h")
    def apagar(self):
        print (f"La Moto: {self.marca} {self.modelo} se apagó")
    
# Creo objetos de la clase Moto

moto1 = Moto("Suzuki", "Vespa", "2000", "Rojo", "Scooter")
moto2 = Moto("Akt", "Nkd", "2022", "Azul", "Naked")
moto3 = Moto("Yamaha", "Mt015", "2024", "Naranja", "Sport")

# Mostrar detalles de los objetos

moto1.mostrar_detalles()
moto2.mostrar_detalles()
moto3.mostrar_detalles()

# Usar metodo de clase

moto1.encender()
moto1.apagar()

moto2.encender()
moto2.apagar()