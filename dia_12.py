# 12 - JSON y XML
import os
import xml.etree.ElementTree as xml # Libreria para manupular xml
import json # # Libreria para manupular JSON

data = {
    "name": "Matias",
    "age": 27,
    "birthday_date":  "09/02/1997",
    "programming_languages": ["Python", "Javascript", "C#"]
}

xml_file = "data.xml"
json_file = "data.json"

# XML
def save_xml():
    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value) 

    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON
def save_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

save_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

"""
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""
save_xml()
save_json()

class Data:
    def __init__(self, name, age, birthday_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birthday_date = birthday_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birthday_date = root.find("birthday_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birthday_date, programming_languages)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birthday_date"],
        json_dict["programming_languages"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)