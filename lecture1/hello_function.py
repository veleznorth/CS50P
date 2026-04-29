
def main():
    hello()
    hello(input_name())    


def input_name():
    name=input("¿Cual es tu nombre? ")
    
    return name

def hello(to="world"):
    print(f"¡Hello! {to}")

main()
