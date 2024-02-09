#!/usr/bin/python3
"""Module for matrix division function.

This module provides a function to divide all elements of a matrix by a
divisor. The matrix must be a list of lists containing integers or floats,
and the divisor must be a non-zero integer or float. Validates the matrix
structure, ensures all rows have the same size, and checks for valid divisor
value.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Validates the matrix structure and the divisor, then performs the
    division, rounding the results to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
            if the divisor is not an integer/float, or if rows have varying sizes.
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list of lists of float: A new matrix with all elements divided by div,
        rounded to 2 decimal places.
    """

    # Validate matrix structure and contents
    if not all(isinstance(row, list) for row in matrix) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(num / div, 2) for num in row] for row in matrix]


#!/usr/bin/python3
"""Module for matrix division function.

This module provides a function to divide all elements of a matrix by a
divisor. The matrix must be a list of lists containing integers or floats,
and the divisor must be a non-zero integer or float. Validates the matrix
structure, ensures all rows have the same size, and checks for valid divisor
value.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Validates the matrix structure and the divisor, then performs the
    division, rounding the results to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
            if the divisor is not an integer/float, or if rows have varying sizes.
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list of lists of float: A new matrix with all elements divided by div,
        rounded to 2 decimal places.
    """

    # Validate matrix structure and contents
    if not all(isinstance(row, list) for row in matrix) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(num / div, 2) for num in row] for row in matrix]
