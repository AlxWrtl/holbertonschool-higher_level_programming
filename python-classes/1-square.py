#!/usr/bin/python3
"""Module for Square class definition.

This module defines a Square class for representing squares with a
customizable size. It includes an initializer to set the size of the square.
"""


class Square:
    """Represents a square with customizable size."""

    def __init__(self, size):
        """Initialize a new Square instance with a specific size.

        Args:
            size: The size of the square's sides.
        """
        self.__size = size
