#!/usr/bin/python3
"""
The 4-print_square module

It prints a square
"""


def print_square(size):
    """ it uses '#' to print a square """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            for i in range(size):
                print('#', end='')
            print()
