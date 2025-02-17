"""
* EJERCICIO:
* ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
* ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
* entre las razas de la Tierra Media?
* Desarrolla un programa que se encargue de distribuirlos.
* Requisitos:
* 1. Los Elfos recibirán un número impar.
* 2. Los Enanos un número primo.
* 3. Los Hombres un número par.
* 4. Sauron siempre uno.
* Acciones:
* 1. Crea un programa que reciba el número total de anillos
*    y busque una posible combinación para repartirlos.
* 2. Muestra el reparto final o el error al realizarlo.
"""
def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def distribute_rings(total_rings: int):
    
    sauron = 1
    total_rings -= sauron # sauron

    distributed_rings = []

    for men in range(2,total_rings,2):
        for elves in range(1,total_rings,2):
            dwarves = total_rings - men - elves
            if dwarves > 0 and is_prime(dwarves):
                distributed_rings.append({
                    "Hombres":men,
                    "Elfos":elves,
                    "Enanos":dwarves,
                    "Sauron":1
                })

    if distributed_rings:
        return distributed_rings

    

    return "No es posible repartir los anillos."



try:
    total_rings = int(input("Ingresa el número total de anillos: "))
    distributed_rings = distribute_rings(total_rings)
    
    if isinstance(distributed_rings, list):
        print("Posibles reparticiones de anillos:\n")
        
        for index, distributed in enumerate(distributed_rings):
            print (f"Combinación {index + 1}: {distributed}")
        
        print ()

        print (f"Destribucion media: {distributed_rings[len(distributed_rings) // 2]}")


    else:    
        print(distributed_rings)

except ValueError:
    print("Ingresa un número válido de anillos.")
