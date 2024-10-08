# Clase padre con método abstracto
class Profesion:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia
    
    def trabajar(self):
        pass
    

# Clase hija Médico
class Medico(Profesion):
    def __init__(self, nombre, experiencia, especialidad):
        super().__init__(nombre, experiencia)
        self.especialidad = especialidad

    def trabajar(self):
        print(f"Médico: {self.nombre}, Años de experiencia: {self.experiencia}, Especialidad: {self.especialidad}, Trabajo: Diagnosticar y tratar pacientes.\n")


# Clase hija Ingeniero
class Ingeniero(Profesion):
    def __init__(self, nombre, experiencia, campo):
        super().__init__(nombre, experiencia)
        self.campo = campo

    def trabajar(self):
        print(f"Ingeniero: {self.nombre}, Años de experiencia: {self.experiencia}, Campo: {self.campo}, Trabajo: Diseñar y construir soluciones técnicas.\n")


# Clase hija Docente
class Docente(Profesion):
    def __init__(self, nombre, experiencia, materia):
        super().__init__(nombre, experiencia)
        self.materia = materia

    def trabajar(self):
        print(f"Docente: {self.nombre}, Años de experiencia: {self.experiencia}, Materia: {self.materia}, Trabajo: Enseñar a los estudiantes.\n")


# Creando objetos de las clases hijas
medico1 = Medico("Dr. Juan", 10, "Cardiología")
ingeniero1 = Ingeniero("Ing. Ana", 7, "Sistemas")
docente1 = Docente("Prof. Laura", 15, "Matemáticas")

medico1.trabajar()
ingeniero1.trabajar()
docente1.trabajar()
