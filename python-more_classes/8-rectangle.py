#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It supports calculating area, perimeter,
instance comparison, and visual representation. Tracks instance count and
allows symbol customization for string representation.
"""


class Rectangle:
    """A class to represent a rectangle with customizable dimensions.

    Class Attributes:
        number_of_instances (int): Counts the Rectangle instances.
        print_symbol (any): Symbol for string representation.

    Instance Attributes:
        width (int): Width of the rectangle, non-negative integer.
        height (int): Height of the rectangle, non-negative integer.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle, defaults to 0.
            height (int): Height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the rectangle's width with validation."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width with validation.

        Args:
            value (int): New width, must be integer >= 0.

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
        """Get or set the rectangle's height with validation."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height with validation.

        Args:
            value (int): New height, must be integer >= 0.

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
        """Return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle's perimeter, or 0 if width/height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation using `print_symbol`."""
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        return "\n".join([line] * self.height)

    def __repr__(self):
        """Return a formal string for recreating the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message upon deletion and update instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determine and return the rectangle with the greater or equal area.
        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.
        Raises:
            TypeError: If either argument is not an instance of Rectangle.
        Returns:
            Rectangle: The rectangle with the bigger or equal area.
        """
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_1 and rect_2 must be instances of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
