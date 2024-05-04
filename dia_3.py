# 3 - Estructuras de datos

# Lista  |  [ ]
my_list = ["Mati", "Juan", "Alvaro", "Lucia"]
print(my_list)
my_list.append("Mica")  # Agregar datos | Al final
print(my_list)
my_list.remove("Alvaro")  # Elimina un dato
print(my_list)
my_list[1] = "Fernando"  # Actualiza un dato
print(my_list)
my_list.sort()  # Ordena de manera alfabética por defecto
print(my_list)
print(type(my_list))

# Tuplas | Inmutable | ( )
my_tuple = ("Mati", "Age", "Address")
print(my_tuple[2])  # Operacion de acceso
my_tuple = tuple(sorted(my_tuple))  # Ordena una tupla
print(my_tuple)
print(type(my_tuple))

# Sets | Estructura desordenada | { }
my_set = {"Mati", "Age", "Address"}
print(my_set)
my_set.add("CP")  # Agrega un dato
my_set.add("CP")  # No permite duplicados
print(my_set)
my_set.remove("Age")  # Eliminar datos
print(my_set)
my_set = set(sorted(my_set))  # LOS SETS NO SE PUEDEN ORDENAR
print(my_set)
print(type(my_set))

# Diccionario | Clave : Valor  | { c : v }
my_dict = {"name": "Matias", "alias": "MB", "address": "Cordoba"}
print(my_dict["name"])  # Acceder a un valor
my_dict["email"] = "mati@gmail.com"  # Agregar datos
print(my_dict)
my_dict["alias"] = "EmeBe"  # Actualiza un dato
print(my_dict)
del my_dict["alias"]  # Eliminar datos

print(my_dict)
print(type(my_dict))


"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""


def agenda():

    def comparar_numero():
        phone = input("Indique el telefono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda_dic[name] = phone
        else:
            print("El numero de telefono debe tener menos de 11 digitos")

    agenda_dic = {}

    while True:
        print("1 - Agregar contacto")
        print("2 - Buscar contacto")
        print("3 - Actualizar contacto")
        print("4 - Borrar contacto")
        print("5 - Finalizar")

        opc = input("Selecciona alguna de las opciones: ")
        match opc:
            case "1":
                name = input("Indique el nombre: ")
                comparar_numero()
            case "2":
                name = input("Indique el nombre a buscar: ")
                if name in agenda_dic:
                    print(f"El numero de telefono del contacto {name} es: {agenda_dic[name]}")
                else:
                    print(f"No se encontro el contacto: {name}")
            case "3":
                name = input("Indique el nombre a actualizar: ")
                if name in agenda_dic:
                    comparar_numero()
            case "4":
                name = input("Indique el nombre a borrar: ")
                if name in agenda_dic:
                    del agenda_dic[name]
                else:
                    print(f"No se encontro el contacto: {name}")
            case "5":
                print("Salir de la agenda")
                break
            case _:
                print("Opcion no valida")

agenda()
