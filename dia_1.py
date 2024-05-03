# 1 - Operadores y estructuras de control

# Operadores aritmeticos 
print (f"Suma: 10 + 5 = {10 + 5}")
print (f"Resta: 10 - 5 = {10 - 5}")
print (f"Mul: 10 * 5 = {10 * 5}")
print (f"Div: 10 / 3 = {10 / 3}")
print (f"Resto: 10 % 3 = {10 % 3}") 
print (f"Exponente: 10 ** 3 = {10 ** 3}") 
print (f"Div entera: 10 // 3 = {10 // 3}") 

# Operadores de comparacion
print (f"Igualdad: 10 == 3 = {10 == 3}")
print (f"Desigualdad : 10 != 3 = {10 != 3}")
print (f"Mayor que: 10 > 3 = {10 > 3}")
print (f"Menor que: 10 < 3 = {10 < 3}")
print (f"Mayor o igual que: 10 >= 10 = {10 >= 10}")
print (f"Menor o igual que: 10 <= 3 = {10 <= 3}")

# Operadores logicos
print (f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print (f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print (f"NOT !: not 10 + 3 == 13 es {not 10 + 3 == 13}")

# Operadores de asignacion
my_num = 11 # Asignacion (=)
print(my_num) 
my_num += 1 # Suma y asignacion (+=)
print(my_num)
my_num -= 1 # Resta y asignacion (-=)
print(my_num) 
my_num *= 2 # Multiplicacion y asignacion (*=)
print(my_num) 
my_num /= 2 # Division y asignacion (/=)
print(my_num)
my_num %= 2 # Resto y asignacion (%=)
print(my_num) 
my_num **= 1 # Exponente y asignacion (**=)
print(my_num)
my_num //= 1 # Division entera y asignacion (//=)
print(my_num)

# Operadores de identidad
my_new_num = 1.0
print (f"my_num is my_new_num es {my_num is my_new_num}") # Compara el valor en memoria (Ocupan diferentes direcciones de memoria)
my_new_num = my_num
print (f"my_num is my_new_num es {my_num is my_new_num}") # True 
print (f"my_num is not my_new_num es {my_num is not my_new_num}") # False

# Operadores de pertenencia
print (f"'i' in 'Mati' = {'i' in 'Mati'}")
print (f"'h' not in 'Mati' = {'h' not in 'Mati'}")

# Operadores de bit 
a = 10 # 1010
b = 3 # 0011
print (f'AND: 10 & 3 = {10 & 3}') # Compara bit a bit: 0010 = 2 | lo transforma y nos da el numero 2 
print (f'OR: 10 | 3 = {10 | 3}') # Compara bit a bit, SI AL MENOS UNO DE LOS DOS BITS ES 1 EL RESULTADO ES 1: 1011  = 11
print (f'XOR: 10 ^ 3 = {10 ^ 3}') # Compara bit a bit, SI LOS BITS SON DIFERENTES ES 1, SI SON IGUALES ES 0 : 1001 = 9
print (f'NOT: ~10 = {~10}') # Invierte el resultado BIT a BIT 
print (f'Desplazamiento a la derecha : 10 >> 2 = {10 >> 2}') # Desplaza los bist = 0010
print (f'Desplazamiento a la izquierda : 10 << 2 = {10 << 2}') # Desplaza los bist  = 101000

# Estructuras de control

# Estructuras de control condicionales
my_string = "Matias"
if my_string == "Mati":
    print("my_string es igual")
elif my_string == "Juan":
    print("my_string es Juan")
else:
    print("my_string no tiene coincidencias ")

# Estructuras de control iterativas (Bucles) 

# FOR
for i in range(11): 
    print(i)

#WHILE
i = 0
while i <= 10:
    print(i)
    i += 1

# Estructura de control para manejar excepciones 
try: # Si se produce un error en este bloque 
    print (10 / 0)
except: # Se ejecuta la excepcion
    print("Se ha producido un error")
finally: # Se ejecuta cuando finaliza independientemente si se ejecuta  "try" o "except"
    print("Finalizo el manejo de excepciones")

"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
j = 10
while j <= 55:
    if j % 2 == 0:
        if j != 16 and j % 3 != 0:
            print (j)
    j += 1