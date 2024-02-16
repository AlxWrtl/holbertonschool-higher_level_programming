#!/usr/bin/python3
"""Module for file writing function.

This module defines a function for writing text to a file, allowing for custom
file paths and text content. The file is written with UTF-8 encoding,
supporting a wide range of characters.
"""


def write_file(filename="", text=""):
    """Write text to a file.

    Opens or creates a file using the provided filename (or uses a default name
    if not provided), writes the specified text to the file, and ensures the
    file is properly closed after writing. The text is written using UTF-8
    encoding.

    Args:
        filename (str): Path to the file where the text will be written.
                        Defaults to an empty string, implying a default
                        filename if applicable.
        text (str): The text to be written to the file. Defaults to an empty
                    string if no text is provided.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
