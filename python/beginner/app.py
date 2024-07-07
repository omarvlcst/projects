# Tested in Python3.12, didn't work in Python3.9

import requests

base_url = "https://pokeapi.co/api/v2/pokemon"

pokemon = input("Dame un Pokemon ").lower()
#pokemon = "ditto"

resultado = requests.get(f"{base_url}/{pokemon}")

respuesta = resultado.json()

tipos_de_pokemon = []
for tipo in respuesta["types"]:
    tipos_de_pokemon.append(tipo["type"]["name"])

habilidades = []
for habilidad in respuesta["abilities"]:
    habilidades.append(habilidad["ability"]["name"])

set_de_movimientos = []
for movimiento in respuesta["moves"]:
    set_de_movimientos.append(movimiento["move"]["name"])

#.title() es para poner la primera letra en mayúscula
print(f"""
Nombre: {respuesta["name"].title()}  
Número en la Pokédex: {respuesta['id']}
Peso: {respuesta["weight"]/10} Kg
Altura: {respuesta["height"]/10} metros
Tipos: {' / '.join(tipos_de_pokemon)}
Habilidades: {' / '.join(habilidades)}
Set de movimientos: \n{'\n'.join(list(map(lambda x: f'- {x}',set_de_movimientos)))}
      """)

#print(respuesta)
#print(respuesta["abilities"])
#ps aux | grep code
