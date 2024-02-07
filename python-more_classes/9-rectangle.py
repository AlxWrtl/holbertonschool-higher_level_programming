#!/usr/bin/python3
"""Module for Rectangle class definition.

This module defines a Rectangle class for representing rectangles with
customizable width and height. It includes properties for width and height
with validation, methods to calculate the area and perimeter, and provides
string representations for easy debugging. Additionally, it offers a class
method to create a square and a custom destructor that prints a message upon
an instance's deletion.
"""


class Rectangle:
    """Represents a rectangle with customizable width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with width and height.

        Ensures that width and height are non-negative integers.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.
        """
        self.width = width  # Calls the width setter
        self.height = height  # Calls the height setter

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle with validation."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Ensures width is a non-negative integer.

        Args:
            value (int): The new width of the rectangle.

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
        """int: Gets or sets the height of the rectangle with validation."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Ensures height is a non-negative integer.

        Args:
            value (int): The new height of the rectangle.

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
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns 0 if either width or height is 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Provide a string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Provide a formal string representation to recreate the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    @classmethod
    def square(cls, size):
        """Create a new Rectangle instance as a square with equal sides.

        Args:
            size (int): The size of each side of the square.

        Returns:
            Rectangle: A new Rectangle instance with width and height
            equal to size.
        """
        return cls(size, size)

    def __del__(self):
        """Print a message upon deletion of the Rectangle instance."""
        print("Bye rectangle...")
