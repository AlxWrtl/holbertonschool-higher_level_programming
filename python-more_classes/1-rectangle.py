#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It supports getting and setting width and
height with property decorators for encapsulation.
"""


class Rectangle:
    """A class to represent a rectangle with customizable dimensions.

    Instance Attributes:
        __width (int): Width of the rectangle, non-negative integer.
        __height (int): Height of the rectangle, non-negative integer.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle, defaults to 0.
            height (int): Height of the rectangle, defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width.

        Args:
            value (int): New width, must be integer >= 0.
        """
        self.__width = value

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height.

        Args:
            value (int): New height, must be integer >= 0.
        """
        self.__height = value
