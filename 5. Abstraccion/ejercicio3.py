"""
Ejercicio 3: Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea(). 
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el método 
realizar_tarea() de manera específica según su especialidad.
"""
from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return "Realizar planeación y supervición de proyectos."

class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "Diagnosticar y tratar a pacientes."

# Uso de las clases
ingeniero = Ingeniero()
print(f"Tarea del ingeniero: {ingeniero.realizar_tarea()}")

doctor = Doctor()
print(f"Tarea del doctor: {doctor.realizar_tarea()}")
