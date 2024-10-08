# Clase Padre
class Electrodomestico:
    # Constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input(f"Ingrese el numero de kWh que consume el refrigerador : "))

    # Metodos publicos
    def registrar(self):
        print(f"""
              ---------------------------
              Electrodomestico registrado 
              ---------------------------
              Marca: {self.marca}
              Color: {self.color}
              Capacidad: {self.capacidad} lt
              Consumo: {self.consumo_electrico} kWh
              ---------------------------
              """)

class Refigerador(Electrodomestico): # subclase 
    #constructor Subclase
    def __init__(self, marca, color, capacidad, tipo_refrigerador):
        super().__init__(marca, color,capacidad) # Superclase Heredada
        self.tipo_refrigerador = tipo_refrigerador # Atributo de la subclase
        self.temperatura = int(input("Ingresar temperatura del electrodomestico en °C: ")) # Atributo local
    
    # Metodos propios de la subclase
    def ajustar_temperatura(self):
        if self.temperatura > 4:
            print(f"La temperatura {self.temperatura} °C se encuentra muy alta ajustando...")
            self.temperatura =4
            print(f"Temperatura ajustada a {self.temperatura} °C \n")
        elif self.temperatura < -4:
            print(f"La temperatura {self.temperatura} °C se encuentra muy baja ajustando...")
            self.temperatura =0
            print(f"Temperatura ajustada a {self.temperatura} °C \n")
        else:
            print(f"La lectura de la temperatura presena error, enviar a servicio tecnico!")

# Instanciando la subclase Refrijerador

refrigerador = Refigerador("Samsung", "Negro", 60, "No Frost")
refrigerador.registrar()
refrigerador.ajustar_temperatura()
