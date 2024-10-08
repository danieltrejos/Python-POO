# Defino clase
class Empleado:
    # Defino Constructr
    def __init__(self, nombre, puesto, salario,area,antiguedad):
        # Defino atributos de la clase
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.area = area
        self.antiguedad = antiguedad
    # Defino metodo para mostrar detalles de la clase
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: ${self.salario}")
        print(f"Área: {self.area}")
        print(f"Antiguedad: {self.antiguedad} años")
        print ("------------------------------------------------------")
    # Metodos de clase
    def trabajar(self):
        print(f"El trabajador: {self.nombre} empezó a trabajar")
    def tomar_vacaciones(self):
        print(f"El trabajador: {self.nombre} se fue un mes de vacaciones")
    
# Creo instancias de la clase

empleado1 = Empleado("Maria", "Jefe Presupuesto", "5000000", "Presupuesto", "5 años")
empleado2 = Empleado("Pedro"," Auxiliar","1300000", "Compras", "1 Año")
empleado3 = Empleado("Manuel", "Asistente","2600000", "Ventas", "3 Años")

# Mostrar detalles de los objetos

empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()

# Usar metodos 

empleado1.trabajar()
empleado1.tomar_vacaciones()