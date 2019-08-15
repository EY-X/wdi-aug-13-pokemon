import json
import requests
import os

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
name = body["name"]
pokemon_id = body["id"]
type = body["types"][0]["type"]["name"]

key = os.environ.get("GIPHY_KEY")
root = 'https://api.giphy.com'
path = '/v1/gifs/search'

url = (f"{root}{path}?api_key={key}&q=pikachu&rating=g")
giphy_res = requests.get(url)
gif_body = json.loads(giphy_res.content)
gif_url = gif_body['data'][0]['images']['fixed_height_still']['url']


print(gif_url)














# def get_pokemon(name):
#     url = f"http://pokeapi.co/api/v2/pokemon/{name}/"
#     res = requests.get(url)
#     return json.loads(res.content)

# pokemon = get_pokemon("pikachu")

# def pokemon_attributes(pokemon):
#     types = [t['type']['name'] for t in pokemon['types']]
    
#     return {
#         'id': pokemon['id'],
#         'name': pokemon['name'],
#         'types': types,
#     }


# print("Name", pokemon['name'])

# key = os.environ.get("GIPHY_KEY")

# def get_gif(pokemon_name):
#     url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={pokemon_name}&rating=g"
#     res = requests.get(url)
#     body = json.loads(res.content)
#     return body['data'][0]['url']

# test = pokemon_attributes(pokemon)


# print(get_gif("pikachu"))