def add_text():
    text = input("Enter a line of text: ")

    with open("records.txt", "a") as file:
        file.write(text + "\n")


def main():
    add_text()
    print("The text was added successfully.")


if __name__ == "__main__":
    main()