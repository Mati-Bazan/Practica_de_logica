# Principio de Sustitución de Liskov
# Si tenemos una clase con otras coases dentro
# Se alteramos la clase padre, puedo cambiar la clase (Objetos de clase) por la sub-clase y el programa
# tendria que seguir funcionando correctamnete

# incorrecta | No todos los pajaros vuelan
class Bird:
    def fly(self):
        return "Volando"
    
class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollon no vuelan")

# bird = Bird()
# bird.fly()
# chicken = Chicken()
# chicken.fly() | Exception: Los pollon no vuelan

class Bird:
    def move(self):
        return "Moviendo"
    
class Chicken(Bird):
    def move(self):
        return "Caminar"
    
bird = Bird()
print(bird.move()) # Moviendo
chicken = Chicken() 
print(chicken.move()) # Caminar

# Intercambio
bird = Chicken()
print(bird.move()) # Caminar
chicken = Bird() 
print(chicken.move()) # Moviendo

"""
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
* 1. Crea la clase Vehículo.
* 2. Añade tres subclases de Vehículo.
* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
* 4. Desarrolla un código que compruebe que se cumple el LSP.
"""

class Vehicle:

    def __init__(self, speed= 0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad {self.speed}Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad {self.speed}Km/h")

class Car(Vehicle):
    def accelerate(self, increment):
        print("El auto esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El auto esta frenando")
        super().brake(decrement)

class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("El bicicleta esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El bicicleta esta frenando")
        super().brake(decrement)

class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("El moto esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El moto esta frenando")
        super().brake(decrement)

def test_vehicle(vehicle):
    vehicle.accelerate(3)
    vehicle.brake(1)

car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)