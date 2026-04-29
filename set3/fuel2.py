def main():
    while True:
        numbers = extract_fuel_list(input_fuel_fraction())
        if numbers[0] < numbers[1] or (numbers[0] == numbers[1] and numbers[1] != 0):
            percentage = round((numbers[0] / numbers[1]) * 100)

            if percentage <= 1:
                print("E")

            elif percentage >= 99:
                print("F")

            else:
                print(f"{percentage}%")
            break


def extract_fuel_list(my_list):
    str_num1 = ""
    str_num2 = ""
    sep = False
    for str_number in my_list:

        if str_number == "/":
            sep = True
        elif not sep:
            str_num1 += str_number
        elif sep:
            str_num2 += str_number

    return (int(str_num1), int(str_num2))


def input_fuel_fraction():
    # states (0,1,2)

    while True:
        current_state = -1
        number_list = []
        fuel_fraction = input("Fraction: ").strip(" ")
        if len(fuel_fraction) >= 3:
            # DFA implementation that validates the following expression "%/%" % being numbers
            for letter in fuel_fraction:

                if letter.isnumeric():

                    if current_state == -1 or current_state == 1:
                        current_state = 1
                    elif current_state == 2 or current_state == 3:
                        current_state = 3
                    number_list.append(letter)

                elif letter == "/" and current_state == 1:
                    current_state = 2
                    number_list.append("/")

                else:
                    current_state = -1

            if current_state == 3:
                return number_list


main()
