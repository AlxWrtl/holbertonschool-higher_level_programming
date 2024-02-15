#!/usr/bin/python3
"""Module providing a utility function to check object's class type.

This module contains a function `is_kind_of_class` that checks whether a
given object is an instance of, or if the object is an instance of a class
that inherited from, the specified class. It's a straightforward way to
perform type checking and inheritance validation in Python.
"""


def is_kind_of_class(obj, a_class):
    """Determine if `obj` is an instance of `a_class` or a derived class.

    This function uses the built-in `isinstance()` function to check if `obj`
    is an instance of `a_class` or if `obj` is an instance of a class that
    inherited from `a_class`.

    Args:
        obj (object): The object to check.
        a_class (type): The class (or type) to check against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or a class that
        inherited from `a_class`, False otherwise.
    """
    return isinstance(obj, a_class)
