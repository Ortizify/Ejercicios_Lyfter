def read_songs():
    file = open("songs.txt", "r")
    songs = file.readlines()
    file.close()

    return songs


def sort_songs(songs):
    songs.sort()
    return songs


def save_songs(songs):
    file = open("sorted_songs.txt", "w")

    for song in songs:
        file.write(song)

    file.close()


def main():
    songs = read_songs()
    songs = sort_songs(songs)
    save_songs(songs)

    print("The songs were sorted successfully.")


if __name__ == "__main__":
    main()