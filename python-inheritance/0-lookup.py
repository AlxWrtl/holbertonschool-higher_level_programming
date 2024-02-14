#!/usr/bin/python3
"""Module providing a utility function to list object attributes and methods.
"""


def lookup(obj):
    """Return the list of available attributes and methods of `obj`.

    This function utilizes the built-in `dir()` function to retrieve a sorted
    list of attributes and methods belonging to the specified object. It's
    useful for introspection and exploring the capabilities of an object
    dynamically at runtime.

    Args:
        obj (object): The object to introspect.

    Returns:
        list: A list of strings representing the object's attributes and
        methods.
    """
    return dir(obj)
