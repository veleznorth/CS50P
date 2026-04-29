def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ")
        if validate_months(date, months):
            break


def validate_months(date, months):
    try:
        #here we separate month/day/year
        splited_date = date.split("/")
        #month must be greater or equal than 12 same with days
        if 1 <= int(splited_date[0]) <= 12 and 1 <= int(splited_date[1]) <= 31:
            #
            print(
                f"{splited_date[2]}-{int(splited_date[0]):02}-{int(splited_date[1]):02}"
            )
            return True
    #format does not match then we try the other format
    except ValueError, IndexError,TypeError:
        # the format is "mont day, year"
        try:
            splited_date = date.split(" ")
            #we get without comma the string number
            splited_date[1] = splited_date[1].replace(",", "")
            #pass the string number to int
            day = int(splited_date[1])
        # if the conversion goes wrong we pass en re prompt the user
        except Exception:
            pass
        else:
            #final check so days cant be greater than 31
            try:
                if day <= 31 and day>0:
                    print(
                        f"{splited_date[2]}-{months.index(splited_date[0])+1:02}-{int(splited_date[1]):02}"
                    )
                    return True
            except:
                pass


main()
