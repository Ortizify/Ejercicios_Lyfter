import csv


def count_genres():
    genre_counts = {}

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            genre = row[1]

            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

    print("\nGenres found:")

    for genre in sorted(genre_counts):
        print(f"{genre}: {genre_counts[genre]}")


def main():
    count_genres()


if __name__ == "__main__":
    main()