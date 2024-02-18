#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle to represent a square.

    A Square is a special case of a Rectangle where all sides are equal.
    It overrides the area method to calculate the square's area and provides
    a custom string representation.

    Attributes:
        __size (int): Size of the square's sides, must be non-negative.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Validates 'size' using the inherited integer_validator method,
        then initializes the parent Rectangle class with size as both
        width and height.

        Args:
            size (int): Size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
