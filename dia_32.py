"""
EJERCICIO:
* ¡Deadpool y Wolverine se enfrentan en una batalla épica!
* Crea un programa que simule la pelea y determine un ganador.
* El programa simula un combate por turnos, donde cada protagonista posee unos
* puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
* de regeneración y evasión de ataques.
* Requisitos:
* 1. El usuario debe determinar la vida inicial de cada protagonista.
* 2. Cada personaje puede impartir un daño aleatorio:
*    - Deadpool: Entre 10 y 100.
*    - Wolverine: Entre 10 y 120.
* 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
* siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
* 4. Cada personaje puede evitar el ataque contrario:
*    - Deadpool: 25% de posibilidades.
*    - Wolverine: 20% de posibilidades.
* 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
* Acciones:
* 1. Simula una batalla.
* 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
* 3. Muestra qué pasa en cada turno.
* 4. Muestra la vida en cada turno.
* 5. Muestra el resultado final.
"""
import random
import time

deadpool_health = int(input("Ingrese la vida inicial de Deadpool: "))
wolberine_health = int(input("Ingrese la vida inicial de Wolberine: "))

turn = 0
refenerate = False

while deadpool_health > 0 and wolberine_health > 0:

    turn += 1 # 14:25
    print(f"\nTurno {turn}")

    # Deadpool ataca a Wolberine

    if refenerate:
        print("Deadpool no puede atacar en este turno, se esta regenerando")
        refenerate = False
    elif random.random() > 0.2:
        deadpool_damage = random.randint(10, 100)
        print(f"Deadpool ha hecho {deadpool_damage} puntos de daño a Wolberine")
        if deadpool_damage == 100:
            refenerate = True
            print("Deadpool ha hecho un daño crítico a Wolberine y no podra atacrae en el siguiente turno")
    
        wolberine_health -= deadpool_damage

        if wolberine_health <= 0:
            print("La vida de Wolberine ha llegado a 0")
            break
        else:
            print(f"Vida restante de Wolberine: {wolberine_health}")
    else:
        print("Wolberine ha evadido el ataque de Deadpool")

    # Wolberine ataca a Deadpool

    if refenerate:
        print("Wolberine no puede atacar en este turno, se esta regenerando")
        refenerate = False
    elif random.random() > 0.25:
        wolberine_damage = random.randint(10, 120)
        print(f"Wolberine ha hecho {wolberine_damage} puntos de daño a Deadpool")
        if wolberine_damage == 120:
            refenerate = False
            print("Wolberine ha hecho un daño crítico a Deadpool y no podra atacrae en el siguiente turno")
    
        deadpool_health -= wolberine_damage

        if deadpool_health <= 0:
            print("La vida de Deadpool ha llegado a 0")
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_health}")
    else:
        print("Deadpool ha evadido el ataque de Wolberine")

    time.sleep(1)

if deadpool_health > 0:
    print(f"Deadpool ha ganado con {deadpool_health} puntos de vida restantes")
else:
    print(f"Wolberine ha ganado con {wolberine_health} puntos de vida restantes")