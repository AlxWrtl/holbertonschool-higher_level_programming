#!/usr/bin/python3
"""Module extending Python's built-in list with a custom class.
"""


class MyList(list):
    """A subclass of the built-in list with an additional method.

    This class inherits all functionalities of the built-in list class and
    introduces a new method to print the list contents in a sorted manner.
    """

    def print_sorted(self):
        """Print the list elements in ascending order.

        This method sorts the list only for the purpose of printing; it does
        not modify the original order of the list elements. Utilizes the
        built-in `sorted()` function for sorting.
        """
        print(sorted(self))
