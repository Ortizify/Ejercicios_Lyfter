import csv


def get_video_games():
    video_games = []

    number_of_games = int(input("How many video games do you want to enter? "))

    for i in range(number_of_games):
        print(f"\nVideo Game #{i + 1}")

        name = input("Enter the name: ")
        genre = input("Enter the genre: ")
        developer = input("Enter the developer: ")
        esrb_rating = input("Enter the ESRB rating: ")

        video_games.append([
            name,
            genre,
            developer,
            esrb_rating
        ])

    return video_games


def save_to_file(video_games):
    with open("video_games.cvs", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")

        writer.writerow([
            "name",
            "genre",
            "developer",
            "esrb_rating"
        ])

        writer.writerows(video_games)


def main():
    video_games = get_video_games()
    save_to_file(video_games)

    print("\nVideo games saved successfully!")


if __name__ == "__main__":
    main()