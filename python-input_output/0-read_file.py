#!/usr/bin/python3
"""Module for file reading function.

This module defines a function for reading from a file and printing its
contents to the console. It supports custom file paths with default encoding
set to UTF-8.
"""


def read_file(filename=""):
    """Read from a file and print its contents.

    Opens a file using the provided filename (or default name if not provided),
    reads its contents, and prints them to the console. Ensures the file is
    properly closed after reading.

    Args:
        filename (str): Path to the file to be read. Defaults to an empty
                        string, implying a default filename if applicable.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
