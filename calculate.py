a = float(input("Enter the first value: "))
b = float(input("Enter your second value: "))
operation = input("Enter an operation (=, -, *, /): ")

def calculate(a: float, b: float, operation) -> float:
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error. Number divided by o equals 0"
        return a / b
    else:
        return "Invalid operation"
    
result = calculate(a, b, operation)

print(f"\n{a} {operation} {b} = {result}")