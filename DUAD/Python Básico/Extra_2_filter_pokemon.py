import json


def filter_pokemon_by_type():
    with open("pokemon.json", "r") as file:
        pokemon_list = json.load(file)

    pokemon_type = input("Enter the Pokemon type you want to search for: ")

    found = False

    print("\nThe Pokemon of that type are:")

    for pokemon in pokemon_list:
        if pokemon["type"].lower() == pokemon_type.lower():
            print(pokemon["name"])
            found = True

    if not found:
        print("No Pokemon found with that type.")


filter_pokemon_by_type()
