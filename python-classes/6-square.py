#!/usr/bin/python3
"""Module for Square class definition.

This module defines a Square class for representing squares with
customizable size and position. It includes validation for both size and
position, a method to calculate the square's area, and a method to print
the square on the console considering its position.
"""


class Square:
    """Represents a square with customizable size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with size and position.

        Validates that the size is a non-negative integer and the position
        is a tuple of two non-negative integers.

        Args:
            size (int): The size of the square's sides, defaults to 0.
            position (tuple): The (x, y) position of the square,
            defaults to (0, 0).

        Raises:
            ValueError: If size is not a non-negative integer or
            if position does not meet the specified criteria.
        """
        self.size = size
        self.position = position

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
            ValueError: If size is not a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: Gets or sets the position of the square with validation."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Ensures position is a tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i > 0 for i in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.size ** 2

    def my_print(self):
        """Print the square considering its position.

        Uses the "#" character for the square and spaces for the position.
        Prints an empty line if the size is 0.
        """
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
