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

