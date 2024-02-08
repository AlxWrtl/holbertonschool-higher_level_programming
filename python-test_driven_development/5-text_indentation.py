#!/usr/bin/python3
"""Module for text_indentation function.

This module defines a function that prints text with 2 new lines after each
'.' (period), '?' (question mark), and ':' (colon). It ensures the input is
a string and removes leading and trailing spaces on each line.
"""


def text_indentation(text):
    """Prints text with two new lines after '.', '?', and ':'.

    The function also trims leading and trailing spaces from each line. It
    checks if the input is a string before processing.

    Args:
        text (str): The text to be processed and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
    print()
