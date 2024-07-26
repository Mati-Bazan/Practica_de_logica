# Peticiones HTTP
# Llamados a un servidor 
import requests

# Get Post Put Delete.
response = requests.get("https://google.com/")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

"""
Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
terminal al que le puedas solicitar información de un Pokémon concreto
utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""
# Solicitud al usuario
pokemon = input("Introduce el nombre o numero del pokemon: ").lower()

# 
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json() # Datos del pokemon | Diccionario
    print(f"Nombre: ", data["name"])
    print(f"ID: ", data["id"])
    print(f"Peso: ", data["weight"])
    print(f"Altura: ", data["height"])
    print(f"Tipos: ")
    for type in data["types"]:
        print(type["type"]["name"])

    print("Juegos: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Cadena de evoluciones: ")
            
            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print(f"Error: Evoluciones no encontradas | {response.status_code}")

    else:
        print(f"Error: Evoluciones no encontradas | {response.status_code}")

else:
    print(f"Error: Pokemon no encontrado | {response.status_code}")
