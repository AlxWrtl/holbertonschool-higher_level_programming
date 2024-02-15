#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a given class.

    Simplifies the check to a single line by directly returning the result of
    the comparison between the object's type and the specified class. This
    approach eliminates the need for explicit if-else statements.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`, otherwise False.
    """
    return type(obj) is a_class