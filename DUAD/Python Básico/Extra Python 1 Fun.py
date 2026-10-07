def count_character(text, character):
    counter = 0

    for letter in text:
        if letter == character:
            counter += 1

    return counter

text = "programming"
character = input("Enter the character you want to search for: ")

result = count_character(text, character)

print("The character was found", result, "times")