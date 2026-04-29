def main():

    meow(meow_times())


def meow_times():
    
    while True:
        meow_times = int(input("how many times the cat should meow: "))

        if meow_times<0 or meow_times>=100:
            print("Invalid number")
        else:
            break
        
    return meow_times


def meow(times):
    for _ in range(times):
        print("meow")

main()
