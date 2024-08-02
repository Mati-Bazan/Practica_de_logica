# Logs
# grabación secuencial en un archivo

import logging # Importamos el modulo
import time

logging.basicConfig(level=logging.DEBUG, # Nivel desde el cual se muestran los "logging" a los usuarios
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

# Niveles de severidad
logging.debug("Mensaje de DEBUG") # Bajo nivel

logging.info("Mensaje de INFO") # Informacion | Un poco mas alto nivel

logging.warning("Mensaje de WARNING") # Advertencias | Un poco mas alto nivel

logging.error("Mensaje de ERROR") # Error | Un poco mas alto nivel

logging.critical("Mensaje de ERROR CRITICO") # Errores criticos | Alto nivel


"""
Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
y listar dichas tareas.
- Añadir: recibe nombre y descripción.
- Eliminar: por nombre de la tarea.
Implementa diferentes mensajes de log que muestren información según la
tarea ejecutada (a tu elección).
Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
"""

class TaskManager:

    def __init__(self) -> None:
        self.task = {}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        if name not in self.task:
            self.task[name] = description
            logging.info(f"La tarea se agrego: {name}")
        else:
            logging.warning(f"Se intento agregar una tarea existente: {name}")

        logging.debug(f"Numero de tareas: {len(self.task)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        start_time = time.time()
        if name in self.task:
            del self.task[name]
            logging.info(f"La tarea se elimino: {name}")
        else:
            logging.error(f"Se intento eliminar una tarea que NO existente: {name}")

        logging.debug(f"Numero de tareas: {len(self.task)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_task(self):
        start_time = time.time()
        if self.task:
            logging.info("Se va a imprimir la lista de tareas")
            for name, description in self.task.items():
                print(f"{name} - {description}")
        else:
            logging.info("La lista no tiene tareas")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(
            f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")


task_manager = TaskManager()

task_manager.add_task("Pan", "Ir a comprar pan")
task_manager.add_task("Tomate", "Ir a comprar tomates")
task_manager.list_task()
task_manager.delete_task("Tomate")
task_manager.list_task()