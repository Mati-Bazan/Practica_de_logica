# 11 - Manejo de ficheros
import os

file_name = "dia_11.txt"

with open (file_name,"w") as file: # Nombre archivo , "w" para escritura | with: lo abres, as file: y lo asocias a.
    file.write("Matias\n") # Escribe Matias en el fichero dia_11.txt
    file.write("27\n") # Escribe 27 en el fichero dia_11.txt
    file.write("Python") # Escribe Python en el fichero dia_11.txt


with open (file_name,"r") as file: # Permisos de lectura "r"
    print(file.read()) # Imprime Matias | 27 | Python

os.remove(file_name) # Borra el fichero 

"""
Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""
file_name = "dia_11_shop.txt"

open (file_name,"a")

while True:
    print("1. Añadir producto")
    print("2. Consoltar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular la venta total")
    print("7. Calcular la venta por producto")
    print("8. Salir del programa")

    option = input("Selecciona una opcion: ")

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open (file_name,"a") as file: # "a" añadir al fichero en lugar de sobreescribirlo
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Nombre: ")
        with open (file_name,"r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open (file_name,"r") as file: # Lee todo el contenido de file_name
            lines = file.readlines() # se guardo en lines
        with open (file_name,"w") as file: # borra el fichero "w" 
            for line in lines: # Revisa linea por linea 
                if line.split(", ")[0] == name:  # Verifica si es la linea que quiero actualizar "name"
                    file.write(f"{name}, {quantity}, {price}\n") # la actualiza
                else:
                    file.write(line) # Si no es, lo deja como lo teniamos antes
    elif option == "4":
        name = input("Nombre: ")
        with open (file_name,"r") as file:
            lines = file.readlines() 
        with open (file_name,"w") as file:
            for line in lines:
                if line.split(", ")[0] != name: # Si es diferente al "name" lo conservo 
                    file.write(line) # Ingresa la linea que no sea igual    
    elif option == "5":
        with open (file_name,"r") as file:
            print(file.read()) 
    elif option == "6":
        total = 0
        with open (file_name,"r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif option == "7":
        name = input("Nombre: ")
        total = 0
        with open (file_name,"r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una de las opciones disponibles")
