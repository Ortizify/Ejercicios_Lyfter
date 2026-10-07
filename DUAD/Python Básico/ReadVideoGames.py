import csv


def read_video_games():
    with open("video_games.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            print("Name:", row[0])
            print("Genre:", row[1])
            print("Developer:", row[2])
            print("ESRB Rating:", row[3])
            print()


def main():
    read_video_games()


if __name__ == "__main__":
    main()