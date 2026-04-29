def main():
    spacecraft = {
        "name" : "Voyager 1",
    
    }
    spacecraft.update({"distance":0.01,"orbit":"sun"})
    #spacecraft["distance"] = 0.01

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    =======REPORT========

    name:{spacecraft.get("name")}
    distance:{spacecraft.get("distance","unknown")} AU
    orbit:{spacecraft.get("orbit","unknowns")}
    =====================
    """


main()
