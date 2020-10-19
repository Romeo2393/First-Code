num1 = float(input("Enter the First number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")