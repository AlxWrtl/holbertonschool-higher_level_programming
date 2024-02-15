#!/usr/bin/python3
"""Module for Rectangle class inheriting from BaseGeometry.

This module defines a Rectangle class that inherits from BaseGeometry,
including validation of width and height and computing the
area of the rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle, with methods for validation and
    area calculation, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with validated width and height.

        Validates the width and height using the `integer_validator` method
        from BaseGeometry before setting these properties.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle, computed as width * height.
        """
        return self.__width * self.__height
