# Funciones de orden superior
# Funciones que pueden recibir funciones como parametro,
# pueden devolver funciones como resultado

from functools import reduce
from datetime import datetime

# Funcion que recibe una funcion y un parametro
def apply_func(func, x):
    return func(x)

print(apply_func(len, "Matias")) # 6

# Funcion que retorna una funcion 
def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier = apply_multiplier(2)
print(multiplier(5)) # 10

print(apply_multiplier(3)(2)) # 6

# Sistema | Funciones de orden superior en el sistema
numeros = [1, 5, 3, 4, 2]

# map() | recibe una lista y una funcion, aplica la funcion a a lista
def apply_double(n):
    return n * 2

print(list(map(apply_double, numeros))) # [2, 10, 6, 8, 4]

# filter() | recibe una lista y una funcion, aplica la funcion a a lista
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numeros))) # [4, 2]

# sorted()
print(sorted(numeros)) # [1, 2, 3, 4, 5] Por defecto ordena los valores 
print(sorted(numeros, reverse=True)) # [5, 4, 3, 2, 1]
print(sorted(numeros, key=lambda x: -x)) # [5, 4, 3, 2, 1]

# reduce()
def apply_sum(x, y):
    return x + y

print(reduce(apply_sum, numeros)) # 15 | 1+ 2+ 3+ 4+ 5

"""
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
lista de calificaciones), utiliza funciones de orden superior para
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
- Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes 
  que tienen calificaciones con un 9 o más de promedio.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""
students = [
    {"name": "Matias","birthday": "09-02-1997","grades": [6, 7, 9, 6]},
    {"name": "Lucia","birthday": "10-04-1996","grades": [5, 5, 5, 5]},
    {"name": "Lucas","birthday": "23-10-1997","grades": [9, 8, 10, 9]}
]

def average(grades):
    return sum(grades) / len(grades)

# Promedio calificaciones
print(
    list(map(lambda student: {
        "name": student ["name"],
        "average": average(student["grades"])}, students)
    )
)

# Mejores estudiantes
print(
    list(
        map(lambda student: 
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
        )
    )
)

# Nacimiento
print(sorted(students, key=lambda student: datetime.strptime(
    student["birthday"], "%d-%m-%Y"), reverse=True))

# Mayor calificación
print(max(map(lambda student: max(student["grades"]), students)))