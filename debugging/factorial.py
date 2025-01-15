#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.
    """
    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    f = factorial(num)
    print(f)

