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
    
def get_artist_data(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Error al obtener los datos del artista: " + response.json())
    
    results = response.json()
    return {
        "name": results["name"],
        "followers": results["followers"]["total"],
        "popularity": results["popularity"],
    }

def get_artist_top_tracks(token: str, id: str):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Error al obtener las canciones del artista: " + response.json())
    
    results = response.json()
    top_track = max(results["tracks"], key=lambda track: track["popularity"])

    return {
        "name": top_track["name"],
        "popularity": top_track["popularity"],
    }

# 1. Token
token = get_token()

# 2. IDs 
artist1 = search_artist(token, "Oasis")
artist2 = search_artist(token, "Linkin Park")

# 3. Datos

# 3.1. Datos de seguidores y popularidad
artist_uno = get_artist_data(token, artist1)
artist_dos = get_artist_data(token, artist2)

# 3.2. Canción más popular
top_track_uno = get_artist_top_tracks(token, artist1)
top_track_dos = get_artist_top_tracks(token, artist2)

# 4. Comparación
counter_artist_uno = 0
counter_artist_dos = 0

print("\nComparación de artistas\n")
print(f"Nombre: {artist_uno['name']}")
print(f"Nombre: {artist_dos['name']}")

# 4.1. Comparación de seguidores
print("\nComparación de seguidores\n")
print(f"Seguidores {artist_uno['name']}: {artist_uno['followers']}")
print(f"Seguidores {artist_dos['name']}: {artist_dos['followers']}")

if artist_uno['followers'] > artist_dos['followers']:
    print(f"{artist_uno['name']} tiene mas seguidores.")
    counter_artist_uno += 1
else:
    print(f"{artist_dos['name']} tiene mas seguidores.")
    counter_artist_dos += 1

# 4.2. Comparación de popularidad
print("\nComparación de popularidad\n")
print(f"Popularidad {artist_uno['name']}: {artist_uno['popularity']}")
print(f"Popularidad {artist_dos['name']}: {artist_dos['popularity']}")

if artist_uno['popularity'] > artist_dos['popularity']:
    print(f"{artist_uno['name']} es más popular.")
    counter_artist_uno += 1
else:
    print(f"{artist_dos['name']} es más popular.")
    counter_artist_dos += 1

# 4.3. Comparación de canciones
print("\nComparación de cancion\n")
print(f"Cancion {top_track_uno["name"]} {artist_uno['name']}: {top_track_uno['popularity']}")
print(f"Cancion {top_track_dos["name"]} {artist_dos['name']}: {top_track_dos['popularity']}")

if top_track_uno['popularity'] > top_track_dos['popularity']:
    print(f"La cancion {top_track_uno["name"]} de {artist_uno['name']} es más popular.")
    counter_artist_uno += 1
else:
    print(f"La cancion {top_track_dos["name"]} de {artist_dos['name']} es más popular.")
    counter_artist_dos += 1

# 5. Resultado
if counter_artist_uno > counter_artist_dos:
    print(f"\n{artist_uno['name']} es más popular que {artist_dos['name']}.")