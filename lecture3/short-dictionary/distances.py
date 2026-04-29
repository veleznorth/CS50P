distances={
    "voyager 1":163,
    "voyager 2":136,
    "pioneer 10":80,
    "new horizons":58
}


def main():
    for name in distances:
        print(f"{name} : {distances[name]}")


    #Values in meters

    for value in distances.values():
        print(f"meters :{value*149597870700}")




main()
