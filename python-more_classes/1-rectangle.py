#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It includes methods to calculate the area and
perimeter of the rectangle. Width and height values are validated to ensure
they are non-negative integers.
"""


class Rectangle:
    """A class to represent a rectangle with customizable dimensions.

    Instance Attributes:
        __width (int): Private attribute for the rectangle's width.
        __height (int): Private attribute for the rectangle's height.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle, defaults to 0.
            height (int): Height of the rectangle, defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Returns:
            int: width of the rectangle
        """
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
        """
        Returns:
            int: height of the rectangle
        """
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
