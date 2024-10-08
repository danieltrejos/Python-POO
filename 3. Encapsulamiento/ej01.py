# Clase persona con atributos encapsulados o privados

class Persona:
    def __init__(self, nombres, apellidos, identidad, fechanacimiento,sexo):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__identidad = identidad
        self.fechanacimiento = fechanacimiento
        self.sexo = sexo

    # Metodo getter

    def obtener_nombres(self):
        return self.__nombres

    # Metodo getter

    def obtener_apellidos(self):
        return self.__apellidos

    # Metodo getter

    def obtener_identidad(self):
        return self.__identidad

    # Metodo setter
    def establecer_nombres(self, nuevo_nombre):
        self.__nombres = nuevo_nombre

    # Metodo setter

    def establecer_apellidos(self, nuevo_apellido):
        self.__apellidos = nuevo_apellido

    # Metodo mostrar detalles

    def mostrar_detalles(self):
        print(f"Nombres: {self.__nombres}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"Identidad: {self.__identidad}")
        print(f"Fecha de nacimiento: {self.fechanacimiento}")
        print(f"Sexo: {self.sexo}")

# Objeto

persona = Persona("John", "Doe", "123456789", "1990-01-01", "Masculino")

# Mostrar detalles

persona.mostrar_detalles()

print("---------------------------------------------------------------------")

# Imprimir el atributo encapsulado modificando su acceso con getter y setter

persona.establecer_nombres("Daniel")
persona.establecer_apellidos("Trejos")

print(f"Nombres: {persona.obtener_nombres()}")
print(f"Apellidos: {persona.obtener_nombres()}")
print(f"Identidad: {persona.obtener_identidad()}")
print(f"Fecha de nacimiento: {persona.fechanacimiento}")
print(f"Sexo: {persona.sexo}")