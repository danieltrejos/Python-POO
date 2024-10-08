# Clase Padre
class Dispositivo :
    def __init__(self, marca, modelo, año_fabricacion) :
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.capacidad_bateria = int(input("Ingrese la capacidad de la bateria en (mAh): "))
        
    def registrar_mostrar(self):
        print(f"---------------------------\nDispositivo registrado\n---------------------------\nMarca: {self.marca}\nModelo: {self.modelo}\nAño de fabricación: {self.año_fabricacion}\nCapacidad de batería: {self.capacidad_bateria} mAh\n")

# Clase Hija
class Smartphone(Dispositivo) :
        def __init__(self, marca, modelo, año_fabricacion, sistema_operativo) :
            super().__init__(marca, modelo, año_fabricacion)
            self.sistema_operativo = sistema_operativo
            self.tipo_conectividad = input("Ingresar el tipo de conectividad(4G/5G): ")
            self.nivel_baterias = int(input("Ingresar nivel de bateria en mAh: "))
        
        def registrar_mostrar(self):
              super().registrar_mostrar()
              print(f"""Sistema operativo: {self.sistema_operativo}\nTipo de conectividad: {self.tipo_conectividad}""")
        def encender(self):
            if self.nivel_baterias > 0:
                print("Encendiendo el smartphone...")
                print(f"Dispositivo {self.sistema_operativo} encendido...")
            else:
                print("El dispositivo no tiene batería suficiente para encenderse.")

# Instancias

smartphone1 = Smartphone("Samsung", "Galaxy S24", 2024, "Android")
smartphone1.registrar_mostrar()
smartphone1.encender()


