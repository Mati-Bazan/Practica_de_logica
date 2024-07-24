# Iteraciones
# Recorrer un conjunto de elementos 

# For
for i in range(1, 11):
    print(i)

# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Funcion recursiva  
def count_ten(i = 1):
    if i <= 10: # Condicion 
        print(i)
        count_ten(i + 1) # Se llama a si misma 

count_ten()

"""
Escribe el mayor número de mecanismos que posea tu lenguaje
para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

for i in {1,2,3,4,5,6,7,8,9,10}:
    print(i)

for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

for i in {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j"}:
    print(i)

for i in {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j"}.values():
    print(i)

# List Comprehensions
print(*[i for i in range(1, 11)], sep= "\n")

for c in "Python":
    print(c)

for e in reversed([1,2,3,4]):
    print(e)

for f, g in enumerate(sorted(["m", "a", "t", "i"])):
    print(f"Indice: {f}, valor: {g}")