#!/usr/bin/python3
"""Function to indent text after punctuation marks.

    This function takes a string and prints it with two new lines after each
    punctuation mark ('.', '?', ':'). It also ensures that any spaces
    following these punctuation marks are removed before adding the new lines.
"""


def text_indentation(text):

    """Args:
        text (str): The text to be indented. Must be a string.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i + 1 < len(text):
                while i + 1 < len(text) and text[i + 1] == " ":
                    i += 1
            print("", end="")
        i += 1
