#!/usr/bin/python3
"""Module for Square class definition.

This module defines a Square class for representing squares with
customizable size. It includes validation to ensure the size is a non-negative
integer and a method to calculate the square's area.
"""


class Square:
    """Represents a square with customizable size."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a specific size.

        Validates that the size is a non-negative integer.

        Args:
            size (int): The size of the square's sides, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
