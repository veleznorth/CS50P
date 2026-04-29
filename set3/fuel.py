def main():
    while True:

        str_fraction = input("fraction: ")
        vect_fraction = str_fraction.split("/")
        try:
            num1=int(vect_fraction[0])
            num2=int(vect_fraction[1])
            percentage=(num1/num2)*100
            
        except ValueError, IndexError,TypeError,ZeroDivisionError:
            pass
        else:

            if num1<=num2 and num2>0:    
                if  percentage<=1:
                    print("E")   
                elif percentage>=99:
                    print("F")
                else:
                    print(f"{round(percentage)}%")
                break
                
            
                


main()
