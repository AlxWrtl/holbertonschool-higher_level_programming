#!/usr/bin/python3
"""Module for checking object-class equivalence.

This module defines a function to determine if an object is exactly an instance
of a specified class. It streamlines the check by directly comparing the
object's type with the given class, avoiding explicit conditional structures.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    This function simplifies the instance check to a single line, eliminating
    the need for more complex if-else statements by directly comparing the
    object's type to the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`,
        otherwise False.
    """
    return type(obj) is a_class
