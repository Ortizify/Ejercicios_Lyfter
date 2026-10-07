import json


def read_pokemon():
    with open("pokemon.json", "r") as file:
        pokemon_list = json.load(file)

    for pokemon in pokemon_list:
        print("Name:", pokemon["name"])
        print("Type:", pokemon["type"])
        print("Level:", pokemon["level"])
        print("--------------------")


read_pokemon()
