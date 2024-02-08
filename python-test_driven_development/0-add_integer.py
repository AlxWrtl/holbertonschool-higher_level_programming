#!/usr/bin/python3
"""Add two integers or floats, returning an integer result.

    This function takes two arguments, `a` and `b`, which are expected to
    be integers or floats. If either `a` or `b` is not an integer or float,
    a TypeError is raised. The function returns the sum of `a` and `b`,
    converting the result to an integer.
"""


def add_integer(a, b=98):
    """
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add, defaults to 98.

    Returns:
        int: The sum of `a` and `b`, converted to an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
