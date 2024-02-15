#!/usr/bin/python3
"""Determines if an object is an instance of a class that inherited from
a specified class.

This function checks whether the given object `obj` is an instance of a class
that directly or indirectly inherits from `a_class`, excluding objects that are
direct instances of `a_class`.
"""


def inherits_from(obj, a_class):
    """Check if `obj` is an instance of a class inherited from `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if `obj` is an instance of a class that inherits from
        `a_class` and is not a direct instance of `a_class`; False otherwise.
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
