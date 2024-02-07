"""Module for Rectangle class definition.

This module defines a Rectangle class with methods for
initializing a rectangle, calculating its area and perimeter,
and comparing the areas of two rectangles. It uses property
decorators for safe access and modification of width and height
with proper validation.

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
        return self._width

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
        self._width = value

    @property
    def height(self):
        """Get or set the rectangle's height with validation."""
        return self._height

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
        self._height = value

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
        """Return larger area rectangle or rect_2 if areas are equal.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: Larger area rectangle, or rect_2 if areas equal.

        Raises:
            TypeError: If rect_1 or rect_2 not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle) or \
                not isinstance(rect_2, Rectangle):
            raise TypeError("Both arguments must be Rectangle instances")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
