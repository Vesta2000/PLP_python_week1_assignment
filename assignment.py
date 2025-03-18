#Basic Calculator Program
#User inputs two numbers
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

#User inputs a mathematical operation
operation = input('Enter a mathematical operation +. -, *, /: ')
# Perform the operation and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation! Please choose from +, -, *, or /.")
    
