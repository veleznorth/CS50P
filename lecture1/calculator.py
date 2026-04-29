num1=float(input("Enter the first number "))
num2=float(input("Enter the second number "))

result=num1+num2
result_round=round(result,ndigits=2)
print(result)   
print(f"{result_round:,}")