#!/usr/bin/python3
"""Module for converting Python objects to JSON strings.

This module defines a function that takes a Python object and converts it into
a JSON-formatted string using the standard json library. It allows for the
serialization of Python data structures (e.g., dictionaries, lists, numbers,
and strings) into JSON strings, enabling easy storage or transmission of data
in a text-based format.
"""
import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON-formatted string.

    Serializes a Python object to a string in JSON format, allowing for the
    representation of Python data structures as strings in a standardized,
    text-based data exchange format.

    Args:
        my_obj (object): The Python object to be serialized to a JSON string.

    Returns:
        str: A JSON-formatted string representing the original Python object.
    """
    return json.dumps(my_obj)
