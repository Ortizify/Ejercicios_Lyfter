import csv


def get_video_games():
    video_games = []

    n = int(input("How many video games do you want to enter? "))

    for i in range(n):
        print(f"\nVideo game {i + 1}")

        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        rating = input("ESRB Rating: ")

        video_game = {
            "Name": name,
            "Genre": genre,
            "Developer": developer,
            "ESRB Rating": rating
        }

        video_games.append(video_game)

    return video_games


def save_video_games(video_games):
    with open("video_games_tabs.csv", "w", encoding="utf-8", newline="") as file:
        headers = ["Name", "Genre", "Developer", "ESRB Rating"]

        writer = csv.DictWriter(
            file,
            fieldnames=headers,
            delimiter="\t"
        )

        writer.writeheader()
        writer.writerows(video_games)


def main():
    video_games = get_video_games()
    save_video_games(video_games)

    print("\nVideo games saved successfully.")


if __name__ == "__main__":
    main()
    