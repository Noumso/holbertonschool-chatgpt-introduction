#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """
    Print all command-line arguments, including the script name.
    """
    for i in range(len(sys.argv)):
        print(sys.argv[i])

