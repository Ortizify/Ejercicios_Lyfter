import csv


def read_video_games():
    with open("videogames.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            print(f"Name: {row[0]}")
            print(f"Genre: {row[1]}")
            print(f"Developer: {row[2]}")
            print(f"Rating: {row[3]}")
            print()


if __name__ == "__main__":
    read_video_games()
    