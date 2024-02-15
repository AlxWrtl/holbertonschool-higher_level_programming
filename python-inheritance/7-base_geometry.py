#!/usr/bin/python3
"""Extends the BaseGeometry class with validation methods.

This module further enhances the BaseGeometry class by including a method
for validating integer values. This addition aids in ensuring that geometric
shape dimensions and other integer parameters meet specified criteria.
"""


class BaseGeometry:
    """A class that serves as a foundation for geometric shapes, including
    methods for area calculation and integer validation.
    """

    def area(self):
        """Placeholder method to compute the area of a shape.

        Raises:
            Exception: If the method is not implemented in a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer and greater than 0.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
