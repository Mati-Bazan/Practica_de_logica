# Asincronía
# Ejecutar un proceso en segundo plano
import datetime
import time
import asyncio # Permite a una funcion ejecutarse de manera asincrona 

async def task (name: str, duratio: int): # se agrega la palabra reservada "async" antes del "def"
    print(f"Tarea: {name}. Duracion: {duratio}s. Inicio: {datetime.datetime.now()}")

    await asyncio.sleep(duratio) # Se "duerme" nuestra funcion por la "duratio"

    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}")

# Tengo que ejecutar la funcion de una manera asincrona con "asyncio.run()"
asyncio.run(task("Tarea 1", 3))

"""
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""

# "asyncio.gather" permite que las funciones se ejecuten a la vez, en paralelo. 
async def async_tasks(): 
    await asyncio.gather(task("Tarea C", 3), task("Tarea B", 2), task("Tarea A", 1))
    await task("Tarea D", 1)

# "await" en que punto espera el resultado | Espera en este punto el resultado 
# Los "await" SOLO se pueden hacer DENTRO de un contexto de asincronia
asyncio.run(async_tasks())

