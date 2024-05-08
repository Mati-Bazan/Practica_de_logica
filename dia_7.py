# 7 - Pilas y colas

# Pilas (stacks - LIFO)
stack = []
stack.append(1) # [1] push
stack.append(2) # [1, 2]
stack.append(3) # [1, 2, 3]
print(stack)

stack_item = stack[len(stack) - 1] # pop
del stack[len(stack) - 1]

print(stack_item) # 3

print(stack.pop()) # 2 | pop 
print(stack) # [1]

# Colas (queue - FIFO)
queue = []
queue.append(1) # enqueue
queue.append(2)
queue.append(3)

print(queue.pop(0)) # dequeue | 1
print(queue) # [2, 3]

"""
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.
"""

def web_navigation():

    web_stack = []

    while True:
        action = input("Añade una URL o navega con adelante | atras | salir: ")

        if action == "salir":
            print("Saliendo del navegador")
            break
        elif action == "adelante":
            pass # No se puede utilizando PILAS
        elif action == "atras":
            if len(web_stack) > 0:
                web_stack.pop()
        else:
            web_stack.append(action)

        if len(web_stack) > 0:  
            print(f"Estas en la web: {web_stack[len(web_stack) - 1]}")
        else:
            print("Pagina de inicio")

# web_navigation()

def shared_printed():
    printed = []
    while True:
        action = input("Añade un documento, o imprimir | salir: ")

        if action == "salir":
            print("Salio de la impresora")
            break
        elif action == "imprimir":
            if len(printed) > 0:
                print(f"Imprimiendo... {printed.pop(0)}")
        else:
            printed.append(action)

        print(f"Cola de impresión: {printed}")

# shared_printed()