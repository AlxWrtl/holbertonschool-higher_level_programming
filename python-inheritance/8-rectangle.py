#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry.

This module defines a Rectangle class that inherits from BaseGeometry. It
includes an initializer that validates the width and height using the inherited
`integer_validator` method from BaseGeometry, ensuring they meet the defined
criteria before setting them.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle, inheriting from BaseGeometry.

    It initializes the rectangle with width and height, validating each
    using the BaseGeometry's integer_validator method.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        The width and height are validated to be integers greater than 0
        before being set as instance attributes.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
