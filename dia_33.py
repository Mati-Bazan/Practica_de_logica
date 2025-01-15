"""
* EJERCICIO:
* ¡Disney ha presentado un montón de novedades en su D23!
* Pero... ¿Dónde está Mickey?
* Mickey Mouse ha quedado atrapado en un laberinto mágico
* creado por Maléfica.
* Desarrolla un programa para ayudarlo a escapar.
* Requisitos:
* 1. El laberinto está formado por un cuadrado de 6x6 celdas.
* 2. Los valores de las celdas serán:
*    - ⬜️ Vacío
*    - ⬛️ Obstáculo
*    - 🐭 Mickey
*    - 🚪 Salida
* Acciones:
* 1. Crea una matriz que represente el laberinto (no hace falta
* que se genere de manera automática).
* 2. Interactúa con el usuario por consola para preguntarle hacia
* donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
* 3. Muestra la actualización del laberinto tras cada desplazamiento.
* 4. Valida todos los movimientos, teniendo en cuenta los límites
* del laberinto y los obtáculos. Notifica al usuario.
* 5. Finaliza el programa cuando Mickey llegue a la salida.
"""
maze = [
    ["🐭", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🚪"]
]

mickey = [0, 0]

while True:

    print("Hacia donde quieres mover a Mickey")
    print("[w] arriba")
    print("[s] abajo")
    print("[a] izquierda")
    print("[d] derecha")
    direccion = input("Introduce la dirección: ")

    current_row, current_column = mickey
    new_row, new_column = current_row, current_column



    match direccion:
        case "w":
            pass
        case "s":
            pass
        case "a":
            pass
        case "d":
            pass
        case _:
            print("Dirección no válida")
            continue