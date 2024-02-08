#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number
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
