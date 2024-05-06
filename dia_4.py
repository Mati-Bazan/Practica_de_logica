# 4 - Cadenas de caracteres

"""
Operaciones 
"""
s1 = "Hola"
s2 = "Mundo"

# Concatenacion
print(s1 + " " + s2)  # Hola Mundo

# Repeticion
print(s1 * 3)  # HolaHolaHola

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])  # Hola

# longitud
print(len(s2))  # 5

# Slicing | Porcion  [Indice inicial : Indice final (No se cuenta)]
print(s2[1:3])  # Print = un
print(s2[1:])  # Indice 2 hasta el final = undo
print(s2[:3])  # Desde el primer caracter = Mun

# Busqueda
print("Ho" in s1)  # "Ho" en "Hola" = True
print("i" in s1)  # False

# Reemplazar | .replace("Caracter que quiero reemplazar" , "Caracter que ocupara su lugar")
print(s1.replace("o", "a"))  # Hala

# Division | .split("En que caracter se dividira")
print(s2.split("n"))  # ['Mu', 'do']

# Mayúscula y Minúscula
print(s1.upper())  # HOLA
print(s1.lower())  # hola

# Primera letra en mayuscula
print("matias bazan".title())  # Matias Bazan
print("matias bazan".capitalize())  # Matias bazan

# Eliminacion de espacios al principio y al final
print("   matias bazan  ".strip())  # matias bazan

# Busqueda al principio y al final | .startswith("Empieza por...") | .endswith("")
print(s1.startswith("Ho"))  # True
print(s2.endswith("do"))  # True

s3 = "Hola que tal. Como estas?"

# Busqueda de posiciones | .find("Busqueda")
print(s3.find("tal"))  # 9
# 14 | se paso toda la frase a minuscula con lower()
print(s3.lower().find("c"))

# Busqueda de ocurrencias  | Cantidad de veces que se muestra un caracter | .count()
print(s3.lower().count("a"))  # 3

# Formateo
print("Saludo: {} , Para: {}!".format(s1, s2))  # Saludo: Hola , Para: Mundo!

# Interpolacion
print(f"Saludo: {s1} , Para: {s2}!")  # Saludo: Hola , Para: Mundo!

# Transformacion de caracteres a una lista
print(list(s1))  # ['H', 'o', 'l', 'a']

l1 = [s1, ", ", s2, "!"]

# Transformacion de una lista a caracteres | "Criterio de union".join()
print("".join(l1))  # Hola, Mundo!

# Transformaciones numericas
s4 = "123456789"
s4 = int(s4)  # Se transforma a int y se guarda en s4
print(s4)

# Comprobaciones varias
s5 = "23456"
print(s1.isalnum())  # True
print(s1.isalpha())  # True
print(s5.isalpha())  # False
print(s5.isnumeric())  # True

"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos 
- Anagramas
- Isogramas
"""


def check(word1: str, word2: str):
    # Palíndromos | [::-1] Invierte la palabra en pythonm
    print(f"¿La palabra: {word1}, es palíndromo? {word1 == word1[::-1]}")
    print(f"¿La palabra: {word2}, es palíndromo? {word2 == word2[::-1]}")

    # Anagramas | sorted ordena alfabéticamente
    print(f"¿La palabra: {word1}, es un anagrama de la palabra: {word2}? {sorted(word1) == sorted(word2)}")

    # Isogramas
    def isograma(word: str) -> bool:
        word_dict = dict()
        for word in word:
            word_dict[word] = word_dict.get(word, 0) + 1

        isograma = True
        values = list(word_dict.values())
        isograma_len = values[0]
        for word_cont in values:
            if word_cont != isograma_len:
                isograma = False
                break
        return isograma

    print(f"¿La palabra: {word1}, es isograma? {isograma(word1)}")
    print(f"¿La palabra: {word2}, es isograma? {isograma(word2)}")


check("radar", "python")
# check("amor", "roma")
