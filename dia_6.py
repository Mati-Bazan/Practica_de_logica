# 6 - Recursividad 
# Una funcion que se llama a si misma | simil bucle, se ejectura una vez tras otra 

"""
Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
"""

def cuenta_atras(numero: int):
    if numero >= 0: # Condicion 
        print(numero)
        cuenta_atras(numero - 1) # Se llama a si misma
    
cuenta_atras(100)

"""
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
sucesión de Fibonacci (la función recibe la posición).
"""
# Factorial
def factorial(num: int) -> int:
    if num < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num -1)

print (factorial(5))

# Sucesión de Fibonacci
def fibonacci(num:int) -> int:
    if num <= 0:
        print("La posicion tiene que ser mayor a 0")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(4))