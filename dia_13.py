# - Pruebas unitarias
import unittest # Libreria de test para python
from datetime import datetime, date #Fechas 

def sum(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
        raise ValueError("Los argumentos tienen que ser enteros o decimales")
    return a + b

class TestSum(unittest.TestCase): # Los test en python tienen que estar en una clase con "unittest.TestCase"
    def test_sum(self): # Los nombres de las funciones de "test" empiezan con test | self = Contexto
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2) 
        self.assertEqual(sum(0, 0), 0) 
        self.assertEqual(sum(2.5, 2.5), 5) 

    def test_sum_type(self): #Test del tipo de datos que se utilizan
        #Supuestos de uso de cadenas de texto en la funcion sum
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")

# unittest.main() # Ejecuta todos los test que empiezan con "test_"

"""
Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

class TestData(unittest.TestCase):

    #Prepara el contexto | Datos que quiero testear
    def setUp(self) -> None:
        self.data = {
            "name": "Matias Bazan",
            "age": 27,
            "birth_date": datetime.strptime("09-02-97", "%d-%m-%y").date(),
            "programming_languages": ["Python", "JavaScript", "C#"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_date_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

unittest.main()