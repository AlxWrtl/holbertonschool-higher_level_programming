#!/usr/bin/python3
"""Module for loading Python objects from JSON files.

This module defines a function that reads from a file containing JSON-formatted
data and converts it into a Python object using the standard json library. It
facilitates the deserialization of JSON data from files into Python data
structures, such as dictionaries and lists,
for further processing and analysis.
"""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON-formatted file.

    Reads a JSON-formatted file and deserializes its content into a Python
    object (e.g., dictionary, list, string, etc.), enabling the manipulation of
    JSON data using Python data structures.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        object: The Python object resulting from the JSON file deserialization.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
