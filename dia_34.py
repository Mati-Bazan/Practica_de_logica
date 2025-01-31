"""
* EJERCICIO:
* ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
* ¿Alguien se entera de todas las relaciones de parentesco
* entre personajes que aparecen en la saga?
* Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
* Requisitos:
* 1. Estará formado por personas con las siguientes propiedades:
*    - Identificador único (obligatorio)
*    - Nombre (obligatorio)
*    - Pareja (opcional)
*    - Hijos (opcional)
* 2. Una persona sólo puede tener una pareja (para simplificarlo).
* 3. Las relaciones deben validarse dentro de lo posible.
*    Ejemplo: Un hijo no puede tener tres padres.
* Acciones:
* 1. Crea un programa que permita crear y modificar el árbol.
*    - Añadir y eliminar personas
*    - Modificar pareja e hijo
* 2. Podrás imprimir el árbol (de la manera que consideres).
* 
* NOTA: Ten en cuenta que la complejidad puede ser alta si
* se implementan todas las posibles relaciones. Intenta marcar
* tus propias reglas y límites para que te resulte asumible.
"""
class Persona:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []

    def add_partner(self, partner):
        if self.partner is not None:
            print(f"{self.name} ya tiene pareja: {self.partner.name}")
        else:
            self.partner = partner
            partner.partner = self
            print(f"{self.name} y {partner.name} son pareja")

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            print(f"{child.name} es hijo de {self.name}")
        else:
            print(f"{child.name} ya es hijo de {self.name}")

class FamilyTree:

    def __init__(self):
        self.people = {}

    def add_person(self, id, name):
        if id in self.people:
            print(f"La persona con ID {id} ya existe")
        else:
            persona = Persona(id, name)
            self.people[id] = persona
            print(f"La persona con nombre {name}, (ID: {id}) ha sido añadida")

    def remove_person(self):
        pass

    def set_partner(self):
        pass

    def add_child(self):
        pass

    def print_tree(self):
        pass
