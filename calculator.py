#program for  making a calculator
value1 = int(input("Enter the first number : "))
operator = input("Enter a valid operator(+,-,/,*,%) : ")
value2 = int(input("Enter the second number : "))

if operator == "+":
    print(value1+value2)
elif operator == "-":
    print(value1-value2)
elif operator == "/":
    print(value1/value2)
elif operator == "*":
    print(value1*value2)
elif operator == "%":
    print(value1%value2)
else:
    print("Invalid Operator")

