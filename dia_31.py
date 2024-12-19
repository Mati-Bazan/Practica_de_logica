"""
* EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""
class Participant:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self) -> int:
        return hash(self.name, self.country)
        

class Olympics:

    def __init__(self):
        self.events = []
        self.participants = {}

    def register_event(self):
        
        event = input("Introduce el nombre del evento deportivo: ").strip()

        if event in self.events:
            print(f"El evento {event} ya existe")
        else:
            self.events.append(event)
            print(f"El evento {event} fue registrado")

    def register_participant(self):

        if not self.events:
            print("Primero debes registrar un evento")
            return
        
        name = input("Introduce el nombre del participante: ").strip()
        country = input("Introduce el país del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos disponibles:")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")
    
        event_choice = int(input("Selecciona el numero del evento para asignar al participante: ")) - 1

        if event_choice >= 0 and event_choice < len(self.events):

            event = self.events[event_choice]

            if participant in self.participants[event]:
                print(f"El participante {name} de {country}. Ya esta registrado en el evento {event}")
            else:
                self.participants[event].append(participant)
                print(f"El participante {name} de {country}. Fue registrado en el evento {event}")

        else:
            print("Seleccion de evento invalido. El participante no fue registrado")

olympics = Olympics()

print("Simulador JJOO")

while True:

    print()

    print("1. Registro de eventos.")
    print("2. Registro de participantes.")
    print("3. Simulación de eventos.")
    print("4. Creación de informes.")
    print("5. Salir")

    option = input("Selecciona una accion:")

    match option:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant() 
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del simulador")
            break
        case _:
            print("Opcion invalida. Por favor selecciona una nueva")


 