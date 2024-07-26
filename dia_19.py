# Enumeraciones
# Estructura limitada de valores | Conjunto de valores | Enum 

from enum import Enum # Enum

# "Simil" constante dias de la semana
class WeekDay(Enum): # Dato tipo "WeekDay" Solo contiene dias de la semana
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

def get_day(numero: int):
    print(WeekDay(numero).name)

get_day(1) # Lunes

"""
Crea un pequeño sistema de gestión del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order():

    status = OrderStatus.PENDIENTE

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status.name == OrderStatus.PENDIENTE:
            self.status = OrderStatus.ENVIADO
            self.display_status()
        else:
            print("El pedido ya fue ENVIADO o CANCELADO")

    def deliver(self):
        if self.status.name == OrderStatus.ENVIADO:
            self.status = OrderStatus.ENTREGADO
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse")

    def cancel(self):
        if self.status.name != OrderStatus.ENTREGADO:
            self.status = OrderStatus.CANCELADO
            self.display_status()
        else:
            print("El pedido ya fue entregado")

    def display_status(self):
        print(f"El estado del pedido {self.id} esta: {self.status.name}")

order_1 = Order(1)

order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()
