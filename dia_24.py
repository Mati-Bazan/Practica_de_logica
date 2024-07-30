# Patron de diseño | Decoradores
# Funcion que extiende o modifica otra funcion, sin modificar la funcion original.

# Decorador
def print_call(function):
    # Dentro del decorador tenemos la funcion que ejecuta la logica
    def print_function():
        print(f"La funcion '{function.__name__}' ha sido llamada")
        return function # Todos los decoradores retornan la funcion
    
    return print_function # Todos los decoradores retornan la funcion

# Funcion base u original
@print_call # llamado al decorador
def example_function():
    pass # La funcion 'example_function' ha sido llamada

def example_function2():
    pass

def example_function3():
    pass

example_function()
example_function2()
example_function3()

"""
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección.
"""

def call_counter(function):
    def counter_function():
        counter_function.call_cunt += 1
        print(f"La funcion '{function.__name__}' ha sido llamada {counter_function.call_cunt} vez/veces")
        return function

    counter_function.call_cunt = 0
    return counter_function

@call_counter
def example_function4():
    pass

@call_counter
def example_function5():
    pass

# Cada instancia es unica para cada funcion | cada funcion tiene su propio contador
example_function4() # La funcion 'example_function4' ha sido llamada 1 vez/veces
example_function4() # La funcion 'example_function4' ha sido llamada 2 vez/veces
example_function4() # La funcion 'example_function4' ha sido llamada 3 vez/veces
example_function5() # La funcion 'example_function5' ha sido llamada 1 vez/veces
example_function4() # La funcion 'example_function4' ha sido llamada 4 vez/veces