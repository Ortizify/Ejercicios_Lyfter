import json


def load_pokemon(filename):
    with open(filename, "r") as file:
        return json.load(file)


def get_pokemon_information():
    print("\nEnter the new Pokémon information:")

    name = input("Name: ")
    pokemon_type = input("Type: ")
    level = int(input("Level: "))
    weight = float(input("Weight in kilograms: "))

    shiny_answer = input("Is the Pokémon shiny? (yes/no): ").lower()
    is_shiny = shiny_answer == "yes"

    held_item = input("Held item (leave empty if none): ")

    if held_item == "":
        held_item = None

    skills_input = input("Skills separated by commas: ")
    skills = [skill.strip() for skill in skills_input.split(",")]

    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))

    new_pokemon = {
        "name": name,
        "type": [pokemon_type],
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense
        }
    }

    return new_pokemon


def save_pokemon(filename, pokemon_list):
    with open(filename, "w") as file:
        json.dump(pokemon_list, file, indent=4)


def main():
    filename = "pokemon.json"

    pokemon_list = load_pokemon(filename)
    new_pokemon = get_pokemon_information()

    pokemon_list.append(new_pokemon)
    save_pokemon(filename, pokemon_list)

    print("\nThe new Pokémon was saved successfully.")


if __name__ == "__main__":
    main()
    