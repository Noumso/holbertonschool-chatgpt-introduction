#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.
    Args:
        n (int): The number to calculate the factorial of.
    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    """
    Main program entry point. Takes a command-line argument and calculates
    its factorial.
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <non-negative integer>")
            sys.exit(1)

        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)

        result = factorial(num)
        print(result)

    except ValueError:
        print("Error: Please provide a valid non-negative integer.")
        sys.exit(1)

