def main():
    expression = input("Expression: ")
    x,y,z = expression.split(" ")
    

    if y == "/" and z == "0":  
        print("error")
    else:
        final=float(resolver(float(x),y,float(z)))
        print(f"{final:.1f}")



def resolver(num1,operator,num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1/num2
            

main()