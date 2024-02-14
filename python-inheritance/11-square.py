#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
Square = __import__('10-square').Square

class Square(Rectangle):
    """A representation of a square."""

    def __init__(self, size):
        """Initialize the square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
