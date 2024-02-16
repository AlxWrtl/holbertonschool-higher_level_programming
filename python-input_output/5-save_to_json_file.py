#!/usr/bin/python3
"""Module for saving Python objects to JSON files.

This module defines a function that takes a Python object and saves it to a
file in JSON format using the standard json library.
It enables the serialization of Python data structures to JSON,
facilitating easy storage and exchange of
data in a widely supported text-based format.
"""

import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a file in JSON format.

    Serializes a Python object (e.g., dictionary, list, string, etc.) to JSON
    format and writes it to a specified file, creating or overwriting the file
    as necessary. This function simplifies the process of persisting data in
    JSON format for later retrieval or exchange.

    Args:
        my_obj (object): The Python object to be serialized to JSON.
        filename (str): The path to the file where the JSON data will be saved.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
