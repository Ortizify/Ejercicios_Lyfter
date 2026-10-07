import json


def display_pokemon_stats():
    with open("pokemon.json", "r") as file:
        pokemon_list = json.load(file)

    for pokemon in pokemon_list:
        print("Name:", pokemon["name"])
        print("HP:", pokemon["stats"]["hp"])
        print("Attack:", pokemon["stats"]["attack"])
        print("Defense:", pokemon["stats"]["defense"])
        print("--------------------")


display_pokemon_stats()