#!/usr/bin/python3
import sys

def factorial(n):
    """Calculer le factoriel d'un nombre."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Vérifier si un argument a été passé
if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)  # Quitter le programme avec un code d'erreur

try:
    # Tenter de convertir l'argument en entier
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer.")
