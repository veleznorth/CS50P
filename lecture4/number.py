def main():
    print(input_integer())
    print(input_string())


def input_integer():

    while True:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("That is not a number")
        else:
            return num


main()
