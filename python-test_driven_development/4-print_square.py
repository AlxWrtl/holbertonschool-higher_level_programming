#!/usr/bin/python3
"""Module for print_square function.

This module defines a function that prints a square with a given size using
the "#" character. It ensures the size is an integer and non-negative.
"""


def print_square(size):
    """Prints a square with a given size using the "#" character.

    Validates the size to ensure it is an integer and non-negative.

    Args:
        size (int): The size of the sides of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
