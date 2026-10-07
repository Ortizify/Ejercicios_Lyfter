def filter_words(word_list, minimum_length):
    filtered_list = []

    for word in word_list:
        if len(word) > minimum_length:
            filtered_list.append(word)

    return filtered_list


words = ["sky", "sun", "wonderful", "day"]

minimum_length = int(input("Enter the minimum number of letters in the word: "))

result = filter_words(words, minimum_length)

print(result)