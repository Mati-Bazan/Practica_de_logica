"""
EJERCICIO:
* Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
* ¡Dos de las bandas más grandes de la historia están de vuelta!
* Desarrolla un programa que se conecte al API de Spotify y los compare.
* Requisitos:
* 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
* 2. Conéctate al API utilizando tu lenguaje de programación.
* 3. Recupera datos de los endpoint que tú quieras.
* Acciones:
* 1. Accede a las estadísticas de las dos bandas.
*    Por ejemplo: número total de seguidores, escuchas mensuales,
*    canción con más reproducciones...
* 2. Compara los resultados de, por lo menos, 3 endpoint.
* 3. Muestra todos los resultados por consola para notificar al usuario.
* 4. Desarrolla un criterio para seleccionar qué banda es más popular.
"""
import requests
import base64

CLIENT_ID = ""
CLIENT_SECRET = ""

def get_token() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data).json()["access_token"]
    if response.status_code != 200:
        raise Exception("Error al obtener el token: " + response.json())

    return response.json()["access_token"]


def search_artist(token: str, name: str) -> dict:
    url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Error al buscar el artista: " + response.json())

    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0][ "id"]
    else:
        raise Exception(f"El artista {name} no se ha encontrado.")
    

token = get_token()
artist1 = search_artist(token, "Oasis")
artist2 = search_artist(token, "Linkin Park")

print(artist1)
print(artist2)