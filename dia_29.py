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
