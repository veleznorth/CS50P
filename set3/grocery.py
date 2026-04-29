def main():
    grocery_list = []
    while True:
        try:
            item = input("item: ").lower()
        except EOFError:
            break
        else:
            grocery_list.append(item)
    print()
    show_final_list(grocery_list)


def show_final_list(items):
    for item in sorted(set(items)):
        print(f"{items.count(item)} {item.upper()}")


main()
