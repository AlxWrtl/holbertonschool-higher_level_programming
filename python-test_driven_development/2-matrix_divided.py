#!/usr/bin/python3
"""Module for matrix_divided function.

This module defines a function that divides all elements of a matrix by a
divisor. It includes type and value checks for the divisor and elements of
the matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor and round the results.

    Validates the divisor and the matrix structure. Each element is divided
    by the divisor, rounded to 2 decimal places, and a new matrix is returned.

    Args:
        matrix (list of lists of numbers): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If div is not an int or float, or if it's a boolean.
        ZeroDivisionError: If div is zero.
        ValueError: If div is negative.

    Returns:
        list of lists of float: A new matrix with the divided and rounded
        elements.
    """
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0 or div == -0.0:
        raise ZeroDivisionError("division by zero")
    if div < 0:
        raise ValueError("div must be greater than 0")
    return [[round(num / div, 2) for num in row] for row in matrix]
