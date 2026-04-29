def main():
    great_question = input("¿what is the answer of the Great Question of Life? ").lower()
    print(ans_great_qs(great_question))


def ans_great_qs(great_question):
    match great_question:
        case "42" | "forty-two" |"forty two":
            return "yes"
        case _:
            return "no"




main() 