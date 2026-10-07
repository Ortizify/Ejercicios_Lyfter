def count_vowels(text):
    counter = 0
    vowels = "aeiouAEIOU"

    for letter in text:
        if letter in vowels:
            counter += 1

    return counter


sentence = "Hello world"

result = count_vowels(sentence)

print(result)