class Celular():
    # Metodo constructor
    def __init__(self, marca, modelo, sistema_operativo,capacidad_bateria, tamaño_pantalla):
        # Defino los atributos de las instancias de la clase
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.capacidad_bateria = capacidad_bateria
        self.tamaño_pantalla = tamaño_pantalla
    # Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Celular")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Capacidad de Batería: {self.capacidad_bateria}")
        print(f"Tamaño de Pantalla: {self.tamaño_pantalla}")
        print("------------------------------------------------")
    
    # Metodo para encender el celular
    def encender(self):
        # Defino el atributo privado energia solo para el metodo encender
        self.energia = int(input("Digite el valor de carga: "))
        
        # Evaluamos el estado del atributo energia
        if self.energia >0 :
            print(f"El celular {self.modelo} se ha encendido")
            print(f"||||||- {self.energia} %")
        else:
            print("No se puede encender el celular, la carga debe ser mayor a 0")
            print("------------------------------------------------")
    
    def apagar_celular(self):
        print(f"El celular {self.modelo} se ha apagado")
        print("------------------------------------------------")
    
# Creamos los objetos a partir de instanciar la clase Celular
celular1 = Celular("Xiaomi","Poco x4 pro","Android 14","5100mA","6.5 pulg")
celular2 = Celular("Samsung","S23","Android 14","5100mA","7.0 pulg")
celular3 = Celular("Iphone","XR","IOS","3200mA","6.2 pulg")

# Mostramos los detalles de los celulares

celular1.mostrar_detalles()
celular2.mostrar_detalles()
celular3.mostrar_detalles()

celular1.encender()
celular1.apagar_celular()



    




