def main():
    print_column(3)
    print_row(3)
    print("\n")
    print_square(5,2)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    for _ in range(width):
        print("?",end="")

def print_square(height,width):
    # for each row
    for _ in range(width):

        #for each brick in the row
        for _ in range(height):
            #print brick
            print("#",end="")
        #line separator is the same that print()
        print("\n",end="")
main()
