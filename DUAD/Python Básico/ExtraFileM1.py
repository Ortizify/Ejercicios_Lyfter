def read_file():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    text = ""

    for line in lines:
        text += line.replace("\n", " ")

    return text.strip()


def write_file(text):
    with open("output.txt", "w") as file:
        file.write(text)


def main():
    text = read_file()
    write_file(text)
    print("The file was created successfully.")


if __name__ == "__main__":
    main()