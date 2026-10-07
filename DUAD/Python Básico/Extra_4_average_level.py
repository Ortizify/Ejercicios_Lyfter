import json


def calculate_average_level_by_type():
    with open("pokemon.json", "r") as file:
        pokemon_list = json.load(file)

    pokemon_by_type = {}

    for pokemon in pokemon_list:
        for pokemon_type in pokemon["type"]:
            if pokemon_type not in pokemon_by_type:
                pokemon_by_type[pokemon_type] = []

            pokemon_by_type[pokemon_type].append(pokemon["level"])

    for pokemon_type, levels in pokemon_by_type.items():
        average_level = sum(levels) / len(levels)

        print("Type:", pokemon_type)
        print("Average level:", round(average_level, 1))
        print("--------------------")


calculate_average_level_by_type()
