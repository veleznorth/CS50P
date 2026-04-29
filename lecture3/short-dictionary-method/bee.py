def main():

    words = {"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPIC":7}
    print("¡Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    while len(words)>0:
        print(f"There are {len(words)} left!")
        guess=input("Guess a word!: ")

        if guess=="GRAFIC":
            print("ups, you hace discoverd the super word, GOODBYE")
            
            break 
        if guess in words.keys():
            print(f"Nice! you got {words.get(guess)} points")
            words.pop(guess)
            
        

        else:
            print("That is not a valid word")
    final_resume(words)

    

    
def final_resume(words):
    print("the game set was:")
    for key,value in words.items():
        print(f"{key}:{value}")

    


main()
