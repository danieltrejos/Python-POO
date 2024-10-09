"""
Ejercicio 2: Crea una clase abstracta Empleado con un método abstracto calcular_salario(). 
Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras 
que implementen calcular_salario() de manera distinta.
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, pago_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora


# Uso de las clases
empleado_completo = EmpleadoTiempoCompleto(2000)
print(f"Salario del empleado a tiempo completo: {empleado_completo.calcular_salario()}")

empleado_horas = EmpleadoPorHoras(100, 15)
print(f"Salario del empleado por horas: {empleado_horas.calcular_salario()}")
