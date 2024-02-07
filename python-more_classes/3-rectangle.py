#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It supports calculating area, perimeter,
and provides a visual representation of the rectangle using a string of
"#" characters.
"""


class Rectangle:
    """A class to represent a rectangle with customizable dimensions.

    Instance Attributes:
        width (int): Width of the rectangle, non-negative integer.
        height (int): Height of the rectangle, non-negative integer.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

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
        """Provide a string representation of the rectangle.

        Uses "#" to visually represent the rectangle, creating a grid
        based on its width and height.

        Returns:
            str: A string representation of the rectangle.
        """
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.strip()
