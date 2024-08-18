# SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
# Es abierto para la extension y cerrado para la modificación.
# Abierto: Añadir funciones sin modificar el codigo existente.
# Cerrado: El codigo no se tiene que modificar, Pero si extender.
from abc import ABC, abstractmethod # Permite crear clases abstractas y metodos

class Form:
    def draw(self):
        pass

# Extender | No se modifico el codigo origianl "class Form"
class Square(Form):
    def draw(self):
        print("Dibujar cuadrado")

class Circle(Form):
    def draw(self):
        print("Dibujar circulo")

class Triangle(Form):
    def draw(self):
        print("Dibujar triangulo")

"""
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para calcular potencias.
* 4. Comprueba que se cumple el OCP.
"""


class Operation(ABC):

    @abstractmethod
    def execute(serlf, a, b):
        pass


class Addition(Operation):
    def execute(serlf, a, b):
        return a + b

class Substration(Operation):
    def execute(serlf, a, b):
        return a - b
    
class Multiplication(Operation):
    def execute(serlf, a, b):
        return a * b
    
class Division(Operation):
    def execute(serlf, a, b):
        return a / b

# Se agrego despues 
class Power(Operation):
    def execute(serlf, a, b):
        return a ** b

    
class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operacion {name} no esta soportada")
        return self.operations[name].execute(a, b)

calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power()) # Quinta operación

print(calculator.calculate("addition", 10, 2))
print(calculator.calculate("substration", 10, 5))
print(calculator.calculate("multiplication", 10, 4))
print(calculator.calculate("division", 10, 4))
print(calculator.calculate("power", 10, 4)) # Se agrego despues | quinta operación