# 2 - Funciones y alcance

# Funciones definidas por el usuario
# Simple
def greet():
    print("Hola desde una funcion")

greet()

# Con retorno
def return_greet():
    return "Hola desde una funcion con retorno"

print(return_greet())

# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Juan")

# Con argumentos
def arg_greet(greet, name):
    print(f"{greet}, {name}!")

arg_greet("Hi","Juan")
arg_greet(name="Juan", greet="Hi")

# Con un argumento predeterminado
def default_arg_greet(name = "Usuario"):
    print(f"Hola, {name}")

default_arg_greet()

# Con argumentos y retorno
def return_arg_greet(greet, name):
    return f"{greet}, {name}!"

print(return_arg_greet("Hello", "Matias"))

# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Funcion con un numero variable de argumentos 
def variable_arg_greet(*names): # El * indica que le podemos pasar mas de un argumento
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Juan", "Mati", "Mica")

# Funcion con un numero variable de argumentos CON palabra clave 
def variable_key_arg_greet(**names): # El ** indica que cada parametro tendra una clave y un valor 
    for key, value in names.items():
        print(f"{value}, ({key})!")

variable_key_arg_greet(
    language = "Python",
    name = "Matias",
    country = "Arg",
)

"""
Funciones dentro de funciones
"""
def ouder_func():
    def inner_func():
        print("Funcion interna: Hola")
    inner_func()

ouder_func()

"""
Funciones del lenguaje
"""
print(len("Mati"))
print(type("Mati"))
print("mati".upper())

"""
Variable local y global
"""
global_var = "Variable tipo global"
print(global_var)

def hello_language():
    local_var = "Hola"
    print (f"{local_var}, {global_var}")

# print(local_var) | Error
hello_language()


"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def print_num(text_1, text_2):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 + text_2)
        elif i % 3 == 0:
            print(text_1)
        elif i % 5 == 0:
            print(text_2)
        else:
            print(i)
            contador += 1
    return contador 

print (print_num("Primer", "Segundo"))