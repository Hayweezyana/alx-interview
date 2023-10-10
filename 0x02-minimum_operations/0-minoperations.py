#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    if n <= 1:
        return 0

    factors = []
    d = 2

    # Find all prime factors of n
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    operations = 0
    clipboard = 0

    for factor in factors:
        if factor == clipboard:
            clipboard = 0
        elif factor > clipboard:
            operations += 2  # Copy All and Paste
            clipboard = factor
        else:
            operations += 1  # Paste
            clipboard = factor

    return operations
