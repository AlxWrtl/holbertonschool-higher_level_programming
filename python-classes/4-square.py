#!/usr/bin/python3
"""Module for Square class definition.

This module defines a Square class for representing squares with
a customizable size. It includes validation to ensure the size is a
non-negative integer, a method to calculate the square's area, and
property decorators to get and set the size with validation.
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
        self.size = size  # Calls the size setter to validate

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.__size ** 2

    @property
    def size(self):
        """int: Gets or sets the size of the square with validation."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Ensures size is a non-negative integer.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
