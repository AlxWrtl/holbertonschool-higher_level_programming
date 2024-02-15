#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle.

This module defines a Square class that inherits from the Rectangle class,
including validation of size, calculating the area, and providing a string
representation specific to squares.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to represent a square, inheriting from Rectangle.

    It initializes the square with a size, validates the size, then uses
    Rectangle's initializer to set width and height to the same value. It
    overrides the area method and provides a custom string representation.
    """

    def __init__(self, size):
        """Initialize a Square instance with validated size.

        Validates the size using the `integer_validator` method from the
        BaseGeometry class (inherited through Rectangle), then initializes
        the Rectangle with width and height equal to `size`.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square, computed as size squared.
        """
        return self.__size ** 2

    def __str__(self):
        """Provide a string representation of the square.

        Returns:
            str: String representation in the format "[Square] size/size".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
