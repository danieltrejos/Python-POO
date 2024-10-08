# Declaro la clase
class Animal:
    # Creo el constructor de la clase
    def __init__(self, num_patas, color, alimentacion, especie, peso):
        # Defino los atributos de la instancia de la clase
        self.num_patas = num_patas
        self.color = color
        self.alimentacion = alimentacion
        self.especie = especie
        self.peso = peso
    # Metodo para mostrar detalles del objeto   
    def mostrar_detalles(self):
        print("Mostrar detalles del objeto")
        print(f"Número de patas: {self.num_patas}")
        print(f"Alimentacion: {self.alimentacion}")
        print(f"Especie: {self.especie}")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg")
        print("------------------------------------")

    # Metodos de clase
    def comer(self):
        print(f"El animal:{self.especie} esta comiendo...quedó satisfecho")
    def morir(self):
        print(f"El animal:{self.especie} se murio")

# Creo objetos de la clase Animal

animal1 = Animal("4 patas", "Blanco","Herbivoro","Vaca","100 kg")
animal2 = Animal("4 patas", "Gris","Omnivoro","Gato","3 kg")
animal3 = Animal("8 patas", "Negro","Carnivoro","Araña","10 gr")

# Muestro detalles de los animales

animal1.mostrar_detalles()
animal2.mostrar_detalles()
animal3.mostrar_detalles()

animal1.comer()
animal1.morir()