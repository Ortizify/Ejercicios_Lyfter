def convert_to_uppercase():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    with open("uppercase.txt", "w") as output_file:
        for line in lines:
            output_file.write(line.upper())


def main():
    convert_to_uppercase()
    print("The new file was created successfully.")


if __name__ == "__main__":
    main()