def main():
    time = input("What time is it?: ")
    print(meal_time(convert(time)))
    


def convert(time:str):
    hour,minutes = time.split(":")

    #String to number
    hour = float(hour)
    minutes = float(minutes)

    #Minutes to hour

    hour2 = minutes/60

    return hour+hour2

def meal_time(time:float):
    if   7 <= time <=8:
        return "breakfast time"
    elif  12 <= time <=13:
        return "lunch time"
    elif 18<= time <=19:
        return "dinner time"
    else:
        return ""



if __name__ == "__main__":
    main()