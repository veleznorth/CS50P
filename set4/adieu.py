import inflect


def main():
    p = inflect.engine()
    name_list = tuple(prompt_names())
    print()
    print(f"Adieu, adieu, to {p.join(name_list)}")


def prompt_names():
    name_list = []
    while True:
        try:
            name = input("Name:")
        except EOFError:
            return name_list
        else:
            name_list.append(name)


main()
