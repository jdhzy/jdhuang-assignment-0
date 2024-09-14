# Assignment task: Write a python script that adds two numbers together 
# and prints their sum to the command line

def add(a, b):
    assert isinstance(a, (int, float)), "First argument must be a number (int or float)"
    assert isinstance(b, (int, float)), "Second argument must be a number (int or float)"
    print("The sum is", a + b)
    return a + b

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call the add function
    add(num1, num2)
except ValueError:
    print("Please enter valid numbers.")