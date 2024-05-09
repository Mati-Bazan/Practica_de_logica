# 10 - Excepciones

try: # Bloque donde podria ocurrir un error 
    print (10/1)
    my_list = [1,2,3,4]
    print(my_list[4])
except Exception as e: # Bloque que se ejevutara SOLO si ocurre un error en el bloque "try" | Exception as e: tipo de error y se guarda en "e"
    print(f"Error :/ {e}") 

print("Hola, fuera del bloque")

"""
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.
"""

class StrTypeError(Exception): # Creacion de un nuevo tipo de error | hereda de la class "Exception"
    pass

def excepciones(parameters:list):

    if len(parameters) < 3:
        raise IndexError()  # raise | lanzar un erro "A mano"
    elif parameters[0] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    excepciones([1,4,2,3])
except IndexError as e: # Detecta solo IndexError
    print("Se produjo un error")
except ZeroDivisionError as e: # Detecta solo ZeroDivisionError
    print("No se puede dividir por cero")
except StrTypeError as e: # Detecta nuestro error personalizado
    print(f"{e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
else: # Se ejecuta cuando NO se cumple ninguno de los "except"
    print("No se produjo ningun error")
finally: # Se ejecita SIEMPRE cuando finaliza la ejecucion 
    print("El programa finalizo")
