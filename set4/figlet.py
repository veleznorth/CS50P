import random
import sys

from pyfiglet import Figlet, FontNotFound


def main():
    figlet = Figlet()

    # length of the line ignorin python and file name
    new_list = sys.argv[1:]

    match len(new_list):
        case 0:
            random_font_output(figlet)
        case 2:
            selected_font_output(figlet, new_list)
        case _:
            sys.exit("Invalid usage")


def random_font_output(figlet):
    phrase = input("Input: ")
    figlet_fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(figlet_fonts))
    print(figlet.renderText(phrase))


def selected_font_output(figlet, new_list):
    match new_list[0]:
        case "-f" | "--font":
            try:
                figlet.setFont(font=new_list[1])
            except FontNotFound:
                sys.exit("Invalid usage")
            else:
                phrase = input("Input: ")
                print(figlet.renderText(phrase))
        case _:
            sys.exit("Invalid usage")


main()
