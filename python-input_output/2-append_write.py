#!/usr/bin/python3
"""Module for appending text to a file.

This module defines a function for appending text to the end of a file,
supporting custom file paths and text content. It ensures that text is added
without overwriting existing content, using UTF-8 encoding for compatibility
with a broad range of characters.
"""


def append_write(filename="", text=""):
    """Append text to the end of a file.

    Opens or creates a file using the provided filename (or uses a default name
    if not provided) in append mode ('a'), writes the specified text to the end
    of the file, and ensures the file is properly closed after appending. The
    operation uses UTF-8 encoding.

    Args:
        filename (str): Path to the file where the text will be appended.
                        Defaults to an empty string, implying a
                        default filename if applicable.
        text (str): The text to be appended to the file. Defaults to an empty
                    string if no text is provided.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
