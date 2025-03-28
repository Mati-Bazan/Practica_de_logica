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

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()

mickey = [0, 0]

while True:

    print_maze(maze)

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
            new_row = current_row - 1
        case "s":
            new_row = current_row + 1
        case "a":
            new_column = current_column - 1
        case "d":
            new_column = current_column + 1
        case _:
            print("Dirección no válida\n")
            continue

    if new_row < 0 or new_row > 5 or new_column < 0 or new_column > 5:
        print("No puedes moverte fuera del laberinto\n")
        continue
    else:
        if maze[new_row][new_column] == "⬛️":
            print("Hay un obstáculo, no puedes moverte\n")
            continue
        elif maze[new_row][new_column] == "🚪":
            print("¡Felicidades, has encontrado la salida!")
            maze[current_row][current_column] = "⬜️"
            maze[new_row][new_column] = "🐭"
            print_maze(maze)
            break
        else:
            maze[current_row][current_column] = "⬜️"
            maze[new_row][new_column] = "🐭"
            mickey = [new_row, new_column]