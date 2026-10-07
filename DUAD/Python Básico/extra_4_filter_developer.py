import csv


def filter_by_developer():
    developer_name = input("Enter a developer name: ")
    found = False

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        print(f"\nVideo games developed by {developer_name}:")

        for row in reader:
            if row[2].lower() == developer_name.lower():
                found = True

                print(
                    f"- {row[0]} "
                    f"(ESRB Rating: {row[3]}, Genre: {row[1]})"
                )

    if not found:
        print("No video games found for that developer.")


def main():
    filter_by_developer()


if __name__ == "__main__":
    main()