a = float(input("Enter your Number: "))
b = float(input("Enter your Number: "))
op = input("Operation(+,-,*,/): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Cannot be Divided with zero")
    else:
        print(a / b)
else:
    print("Invalid Operation")
