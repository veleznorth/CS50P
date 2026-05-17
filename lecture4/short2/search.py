from package1.artist import get_artists
from package1.artwork import get_artist_work


def main():

    while True:
        try:
            search = input("What search do you whant to do: ").strip()
            match search:
                case "artist":
                    artist = input("Artist: ")
                    # API petition
                    result = get_artists(artist)

                    # PRINT results
                    try:
                        c = 1
                        for artists in result["data"]:
                            print(f"{c}#{artists['title']}")
                            c += 1

                    except TypeError:
                        print("Eror type error")

                    print()
                    break

                case "artwork":
                    art = input("ArtWork: ")

                    # Number validation
                    while True:
                        try:
                            size = int(input("Number of pieces you want: "))
                        except ValueError:
                            print("That is not a valid number")
                        else:
                            break

                    # API petition
                    result = get_artist_work(art, size)

                    # Print results
                    try:
                        c = 1
                        for artwork in result["data"]:
                            print(f"{c}#{artwork['title']}")
                            c += 1

                    except TypeError:
                        print("Eror type error")

                    print()
                    break
                case _:
                    print("Is not a valid option")
        except EOFError:
            print("Goodbye")


main()
