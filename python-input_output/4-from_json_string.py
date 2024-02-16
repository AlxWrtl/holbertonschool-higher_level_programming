#!/usr/bin/python3
"""Module for converting JSON string to Python object.

This module defines a function that takes a JSON-formatted string and converts
it into a Python object using the standard json library. This is useful for
parsing JSON data received as strings into Python data structures for further
manipulation.
"""

import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object.

    Takes a string in JSON format and converts it into a corresponding Python
    object (e.g., dictionary, list, string, etc.), allowing for easy access and
    manipulation of data stored in JSON format.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        object: The Python object resulting from the JSON string conversion.
    """
    return json.loads(my_str)
