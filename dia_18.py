# Conjuntos
# Estructura de datos | almacena ams de un cato 

# Lista
data = [1,2,3,4,5]

# Añade un elemento al final
data.append(6)
print(data) # [1, 2, 3, 4, 5, 6]

# Añade un elemento al principio
data.insert(0, 0) 
print(data) # [0, 1, 2, 3, 4, 5, 6]

# Añade varios elementos en bloque al final
data.extend([7,8,9])
print(data) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Añade varios elementos en bloque en una posición concreta 
data[3:3] = [-1,-2,-3] # slice
print(data) # [0, 1, 2, -1, -2, -3, 3, 4, 5, 6, 7, 8, 9]

# Elimina un elemento en una posición concreta
del data[3]
print(data) # [0, 1, 2, -2, -3, 3, 4, 5, 6, 7, 8, 9]

# Actualiza el valor de un elemento en una posición concreta
data[4] = -1
print(data) # [0, 1, 2, -2, -1, 3, 4, 5, 6, 7, 8, 9]

# Comprueba si un elemento está en un conjunto
print(-1 in data) # True
print(-3 in data) # False

# Elimina todo el contenido del conjunto
data.clear()
print(data) # []

"""
Muestra ejemplos de las siguientes operaciones con conjuntos:
- Unión.
- Intersección.
- Diferencia.
- Diferencia simétrica.
"""
set_1 = {1,2,3,4,5} # () Set = elementos que no se repiten
set_2 = {1,2,3,9,10}

# Unión | NO tiene repetidos
print(set_1.union(set_2)) # {1, 2, 3, 4, 5, 9, 10}

# Intersección | Elementos repetidos en los dos sets
print(set_1.intersection(set_2)) # {1, 2, 3}

# Diferencia | Elementos que SOLO estan en el "set_1" y NO en el "set_2"
print(set_1.difference(set_2)) # {4, 5}
print(set_2.difference(set_1)) # {9, 10}

# Diferencia simétrica | Elementos que no se repiten en los dos SETS
print(set_1.symmetric_difference(set_2)) # {4, 5, 9, 10}
