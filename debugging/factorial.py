#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

# Check if the script is run with the correct arguments
if len(sys.argv) != 2:
    print("Usage: ./script.py <non-negative-integer>")
    sys.exit(1)

try:
    # Convert input to an integer and calculate the factorial
    num = int(sys.argv[1])
    print(factorial(num))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

