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
class Olympics:

    def __init__(self):
        self.events = []

    def register_event(self):
        
        event = input("Introduce el nombre del evento deportivo: ").strip()

        if event in self.events:
            print(f"El evento {event} ya existe")
        else:
            self.events.append(event)
            print(f"El evento {event} fue registrado")
    

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
            olympics.register_event() # 10:15
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del simulador")
            break
        case _:
            print("Opcion invalida. Por favor selecciona una nueva")


 