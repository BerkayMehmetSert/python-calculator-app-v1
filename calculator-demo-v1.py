print("""
This is a simple calculator.
 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n
 """)

choise = input("Enter your choise: ")
if choise == "1":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition is: ", a+b)
elif choise == "2":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction is: ", a-b)
elif choise == "3":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication is: ", a*b)
elif choise == "4":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division is: ", a/b)
else:
    print("Invalid choise")
    