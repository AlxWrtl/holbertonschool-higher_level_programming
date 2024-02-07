#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It includes methods to calculate the area
and perimeter, and supports string representations for both informal and
formal (via __str__ and __repr__) use cases. Width and height values are
validated to ensure they are non-negative integers.
"""


class Rectangle:
    """A class to represent a rectangle with customizable dimensions.

    Instance Attributes:
        __width (int): Private attribute for the rectangle's width.
        __height (int): Private attribute for the rectangle's height.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height.

        Width and height default to 0 if not provided.

        Args:
            width (int): Width of the rectangle, defaults to 0.
            height (int): Height of the rectangle, defaults to 0.
        """
        self.width = width  # Calls the width setter
        self.height = height  # Calls the height setter

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width with validation.

        Args:
            value (int): New width, must be non-negative integer.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height with validation.

        Args:
            value (int): New height, must be non-negative integer.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle's area.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangle's perimeter.

        Returns 0 if either width or height is 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """Provide an informal string representation of the rectangle.

        Uses "#" to visually represent the rectangle based on its dimensions.

        Returns:
            str: A string representation of the rectangle.
        """
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """Provide a formal string representation for recreating the rectangle.

        Returns:
            str: A formal representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
