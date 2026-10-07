import csv


def filter_by_esrb():
    esrb_rating = input("Enter an ESRB rating: ")
    found = False

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[3].upper() == esrb_rating.upper():
                found = True

                print(f"\nName: {row[0]}")
                print(f"Genre: {row[1]}")
                print(f"Developer: {row[2]}")
                print(f"ESRB Rating: {row[3]}")

    if not found:
        print("\nNo video games found with that ESRB rating.")


def main():
    filter_by_esrb()


if __name__ == "__main__":
    main()