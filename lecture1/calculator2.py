def main():
    number=request()
    number_powered=square(number)
    show_power(number_powered)



def request():
    number=int(input("Enter the number you want to power: "))
    return number


def square(number):

    return number**2

def show_power(pw_number):
    print(f"{pw_number:,}")

main()