def count_words():
    with open("input.txt", "r") as file:
        content = file.read()

    words = content.split()

    return len(words)


def main():
    total_words = count_words()
    print("This file contains", total_words, "words.")


if __name__ == "__main__":
    main()