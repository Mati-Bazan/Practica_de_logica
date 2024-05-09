# 9 - Herencia y polimorfismo

# Superclase 
class Animal: 
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# Subclases
class Dog(Animal): # Hereda el comportamiento de "Animal" | Name y reescribe sound()
    def sound(self):
        print("Guau")

class Cat(Animal): # Hereda el comportamiento de "Animal" | Name y reescribe sound()
    def sound(self):
        print("Miau")

def print_sound(animal:Animal): # Un ejemplo de polimorfismo | 
    animal.sound()

my_animal = Animal("Animal")
print_sound(my_animal) # " "
my_dog = Dog("Perro")
print_sound(my_dog) # Guau
my_cat = Cat("Gato")
print_sound(my_cat) # Miau


"""
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""

class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):
    def coordinate(self):
        print(f"{self.name} esta coordinando")

class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project:str):
        super().__init__(id, name)
        self.project = project

    def coordinate(self):
        print(f"{self.name} esta coordinando su proyecto")

class Programmer(Employee):
    def __init__(self, id: int, name: str, language:str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en {self.language}")

    def add(self, employee: Employee):
        print(f"Un programador no tiene empleados a su cargo, {employee.name} no se añadira.")


my_manager = Manager(1,"Pepito")
my_project_manager = ProjectManager(2, "Juan", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Juancito", "Proyecto 2")
my_programmer1 = Programmer(4, "Mati", "Python")
my_programmer2 = Programmer(5, "Mica", "Js")
my_programmer3 = Programmer(6, "Luis", "Java")
my_programmer4 = Programmer(7, "Rous", "Cobol")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer1)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer1.add(my_programmer2) # Un programador no tiene empleados a su cargo, Mica no se añadira.

my_programmer1.code() # Mati esta programando en Python
my_project_manager.coordinate() # Juan esta coordinando su proyecto
my_manager.coordinate() # Pepito esta coordinando
my_manager.print_employees() # Juan | Pepito
my_project_manager.print_employees() # Mati | Mica
my_programmer1.print_employees() # " "