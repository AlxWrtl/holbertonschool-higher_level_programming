#!/usr/bin/python3
"""Module for converting class instances to JSON-compatible dictionaries.

This module defines a function that takes an instance of a class and converts
it into a dictionary that is compatible with JSON serialization. It utilizes
the built-in `__dict__` attribute of class instances to achieve this, enabling
the easy conversion of Python objects to a format
that can be serialized into JSON.
"""


def class_to_json(obj):
    """Convert a class instance to a JSON-compatible dictionary.

    Extracts the `__dict__` attribute from a class instance, which contains all
    the instance's attributes as a dictionary. This dictionary is directly
    compatible with JSON serialization, making it easy to convert
    Python objects to JSON.

    Args:
        obj (object): The class instance to convert to a dictionary.

    Returns:
        dict: A dictionary containing all the instance's attributes, ready for
        JSON serialization.
    """
    return obj.__dict__
