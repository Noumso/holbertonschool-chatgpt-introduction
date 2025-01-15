#!/usr/bin/python3

import sys


def factorial(n):
    """Calculer le factoriel d'un nombre."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
