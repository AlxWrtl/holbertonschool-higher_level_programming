#!/usr/bin/python3
"""Module for generating Pascal's triangle.

This module defines a function to generate Pascal's triangle up to a specified
number of rows. Pascal's triangle is a triangular array of the binomial
coefficients, with each number being the sum of the two numbers
directly above it.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows.

    Creates a list of lists representing Pascal's triangle,
    where each inner list represents a row in the triangle.
    The function handles edge cases by returning an empty
    list for non-positive `n` values.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists: A list containing `n` lists, each representing a row of
        Pascal's triangle.
    """
    if n <= 0:
        return []
    pascal = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        row.append(1)
        pascal.append(row)

    return pascal
