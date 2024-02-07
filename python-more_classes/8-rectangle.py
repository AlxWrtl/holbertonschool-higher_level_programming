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
        number_of_instances (int): Counts the instances.
        print_symbol (any): Symbol for string representation.

    Instance Attributes:
        width (int): Non-negative integer width.
        height (int): Non-negative integer height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize with width and height, defaults to 0."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width property with validation."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation, must be non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height property with validation."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation, must be non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter, or return 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation using `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        pattern = str(self.print_symbol) * self.__width
        return "\n".join([pattern for _ in range(self.__height)])

    def __repr__(self):
        """Formal string for recreating the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Message upon deletion and decrement instance count."""
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
