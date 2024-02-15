#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    This function determines if the object `obj` is an instance of the class
    `a_class` directly, not considering inheritance from subclasses.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
