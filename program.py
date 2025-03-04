def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

def main():
    operations = {'1': add, '2': subtract, '3': multiply, '4': divide}
    print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice(1/2/3/4): ")

    if choice in operations:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        print(f"Result: {operations[choice](num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
