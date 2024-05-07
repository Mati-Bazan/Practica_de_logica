# 5 - Valor y referencia

# Tipos de datos por valor
my_int_a = 10
my_int_b = my_int_a # Copia del valor 
my_int_a = 30
print(my_int_a) # 30
print(my_int_b) # 10

# Tipos de datos por referencia | Heredan su posicion de memoria
my_list_a = [10,20]
my_list_b = my_list_a # Misma direccion de memoria | Los datos estan en un unico lugar 
my_list_b.append(30)
print(my_list_a) # [10, 20, 30]
print(my_list_b) # [10, 20, 30]

# Funciones con datos por valor 
my_int_c = 10
def my_int_func(my_int: int):
    my_int = 30
    print(my_int)

my_int_func(my_int_c) # 30
print(my_int_c) # 10

# Funciones con datos por referencia 
my_list_c = [10,20]
def my_list_func(my_list:list):
    my_list.append(30)

    my_list_d = my_list_c
    my_list_d.append(40)

    print(my_list)
    print(my_list_d) # [10, 20, 30, 40]

my_list_func(my_list_c) # [10, 20, 30, 40]
print(my_list_c) # [10, 20, 30, 40]

"""
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime
  el valor de las variables originales y las nuevas, comprobando que se ha invertido
  su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""
# Por valor 
my_int_d = 10
my_int_e = 20

def value_change(value_a: int, value_b: int):
    temp = value_a
    value_a = value_b
    value_b = temp

    return value_a, value_b

my_int_f, my_int_g = value_change(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}") # 10, 20
print(f"{my_int_f}, {my_int_g}") # 20, 10

# Por referencia 
my_list_d = [10,20]
my_list_e = [30,40]

def ref(value_a: list, value_b: list):
    temp = value_a
    value_a = value_b
    value_b = temp

    return value_a, value_b

my_list_f, my_list_g = ref(my_list_d, my_list_e)

print(f"{my_list_d}, {my_list_e}") # [10, 20], [30, 40]
print(f"{my_list_f}, {my_list_g}") # [30, 40], [10, 20]