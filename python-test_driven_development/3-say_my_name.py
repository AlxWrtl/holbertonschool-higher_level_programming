#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Returns a name as a string
    Args:
        first_name (str): The first name
        last_name (str): The last name
    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return "My name is {} {}".format(first_name, last_name)
