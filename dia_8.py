# 8 - Clases

class Programmer:

    surname: str = None # Parametro opcional 

    def __init__(self, name, age, language):  # Inicializador | VALORES (name, age, language) iniciales 
        self.name = name
        self.age = age
        self.language = language

    def print(self): # Funcion 
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.language}")

my_programmer = Programmer("Matias", "27", ["python", "js"]) # Instancia 
my_programmer.print()
my_programmer.surname = "Bazan"
my_programmer.print()

"""
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas 
en el ejercicio número 7 de la ruta de estudio)
 - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
   retornar el número de elementos e imprimir todo su contenido.
"""
# LIFO
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
my_stack.print()

#FIFO
class Queue:
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)
    
    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
