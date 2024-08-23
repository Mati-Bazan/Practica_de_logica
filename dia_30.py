# Principio de Inversión de Dependencias
# Los modulos de alto nivel no pueden depender de modulos de bajo nivel

# Sin DIP
class Switch:
    def turn_on(self):
        print("Encender lampara")

    def turn_off(self):
        print("Apagar lampara")

class Lamp:

    def __init__(self) -> None:
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = Lamp()
lamp.operate("on")
lamp.operate("off")

# Con DIP
class AbstractSwitch:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LampSwitch(AbstractSwitch):
    def turn_on(self):
        print("Encender lampara")

    def turn_off(self):
        print("Apagar lampara")

class Lamp:

    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")

"""
 Crea un sistema de notificaciones.
 Requisitos:
* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones:
* 1. Crea la interfaz o clase abstracta.
* 2. Desarrolla las implementaciones específicas.
* 3. Crea el sistema de notificaciones usando el DIP.
* 4. Desarrolla un código que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod

class Notifier(ABC):
    def send (self, message: str):
        pass

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando email, {message}")

class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando PUSH, {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS, {message}") 


class NotificationService:

    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)

# service = NotificationService(EmailNotifier())
# service = NotificationService(PUSHNotifier())
service = NotificationService(SMSNotifier())
service.notify("Hola")