# 1. Number -> Word
print("\n--- Program 1: Number to Word ---")

num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")


# 2. Day -> Name
print("\n--- Program 2: Day Name ---")

day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# 3. Simple Calculator
print("\n--- Program 3: Calculator ---")

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")