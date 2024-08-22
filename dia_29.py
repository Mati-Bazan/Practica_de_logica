# Principio de Segregación de Interfaces
# Una clase no tiene que estar obligada a implementar interfaces que no utiliza
# Se tiene que realizxar interfases para cada uno de los metodos

from abc import ABC, abstractmethod

#sin ISP
class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Human(WorkerInterface):
    def work(self):
        print("Trabajando")
    
    def eat(self):
        print("Comiendo")

class Robot(WorkerInterface):
    def work(self):
        print("Trabajando")
    
    def eat(self):
        pass # los robots no comen

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat() # mal

# Con ISP
class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass

class Human(WorkInterface, EatInterface):
    def work(self):
        print("Trabajando")
    
    def eat(self):
        print("Comiendo")

class Robot(WorkInterface):
    def work(self):
        print("Trabajando")

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

"""
Crea un gestor de impresoras.
Requisitos:
* 1. Algunas impresoras sólo imprimen en blanco y negro.
* 2. Otras sólo a color.
* 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
* 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
* 2. Aplica el ISP a la implementación.
* 3. Desarrolla un código que compruebe que se cumple el principio.
"""

class PrinterInterface(ABC):
    @abstractmethod
    def print(self, document:str):
        pass

class ColorPrinterInterface(ABC):
    @abstractmethod
    def print_color(self, document:str):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document:str) -> str:
        pass

class FaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document:str):
        pass 

class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"Imprimiendo en ByN {document}")

class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"Imprimiendo en a color {document}")

class MultifunctionPrinter(PrinterInterface, ColorPrinterInterface, ScannerInterface, FaxInterface):
    def print(self, document: str):
        print(f"Imprimiendo en ByN {document}")

    def print_color(self, document: str):
        print(f"Imprimiendo en a color {document}")

    def scan(self, document:str) -> str:
        print(f"Escaneando el documento: {document}")
        return f"Documento {document} escaneado."

    def send_fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")


def test_printers():
    printer = Printer()
    color_printer = ColorPrinter()
    multifunction_printer = MultifunctionPrinter()

    printer.print("Doc.pdf")
    color_printer.print_color("Doc_2.pdf")
    multifunction_printer.print("Doc_3.pdf")
    multifunction_printer.print_color("Doc_3.pdf")
    multifunction_printer.send_fax("Doc_3.pdf")
    multifunction_printer.scan("Doc_3.pdf")

test_printers()