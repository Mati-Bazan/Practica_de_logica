# Callbacks
# Funcion que se le pasa como parametro a otra funcion
import random # Ejercicio extra 
import time # Ejercicio extra
import threading # Ejercicio extra "EXTRA"

# Funcion que recibe un parametro y otra funcion 
def greeting(name: str, callback):
    print("Ejecutango greeting")
    callback(name)

# Funcion "Normal" con un parametro
def greet_callback(name: str):
    print(f"Hola {name}")
    print("Saludo finalizado")

greeting("Mati", greet_callback)

# Las Callbacks se utilizan sobre todo en programacion asincrona 

"""
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una
de listo y otra de entrega.
- Debe imprimir un confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
- Debe invocar a cada callback siguiendo un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado.
"""

# Funcion primaria 
def order_process(dish_name:str, confirm_callback, ready_callback, delivered_callback):
    def process(): # Extra "EXTRA"
        confirm_callback(dish_name)
        time.sleep(random.randint(1,10)) # "Duerme" la funcion entre 1 y 10 segundos

        ready_callback(dish_name)
        time.sleep(random.randint(1,10)) # "Duerme" la funcion entre 1 y 10 segundos

        delivered_callback(dish_name)
    
    # Extra "EXTRA" permite ejecutar la funcion process de manera asincrona
    threading.Thread(target=process).start()

# Funciones secundarias
def confirm_order(dish_name:str):
    print(f"Tu pedido {dish_name} fue confirmado.")

def order_ready(dish_name:str):
    print(f"Tu pedido {dish_name} esta listo.")

def order_delivered(dish_name:str):
    print(f"Tu pedido {dish_name} ha sido entregado.")

# LLamado
order_process("Pizza napolitana", confirm_order, order_ready, order_delivered)

# Extra "EXTRA"
order_process("Pizza provenzal", confirm_order, order_ready, order_delivered)
order_process("Pizza mozzarella", confirm_order, order_ready, order_delivered)
order_process("Pizza jamon y morron", confirm_order, order_ready, order_delivered)