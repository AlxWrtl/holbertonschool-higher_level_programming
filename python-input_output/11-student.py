#!/usr/bin/python3
"""Module for converting class instances to JSON-compatible dictionaries."""


def __init__(self, first_name, last_name, age):
    """Initialize an instance with first name, last name, and age.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        age (int): The age of the person.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self, attrs=None):
    """Convert instance attributes to a dictionary for JSON serialization.

    If `attrs` is a list of strings, filters the resulting dictionary to only
    include keys matching items in `attrs`.

    Args:
        attrs (list, optional): List of attribute names to include in the
        resulting dictionary. Defaults to None, which includes all attributes.

    Returns:
        dict: A dictionary representation of instance attributes, filtered by
        `attrs` if provided.
    """
    if (isinstance(attrs, list) and
            all(isinstance(item, str) for item in attrs)):
        sorted_dict = {
            key: value for key, value in self.__dict__.items()
            if key in attrs
        }
        return sorted_dict
    return self.__dict__


def reload_from_json(self, json):
    """Update instance attributes with values from a JSON-deserialized object.

    Args:
        json (dict): A dictionary where keys are attribute names and values are
        the corresponding values to set on the instance.
    """
    for key, value in json.items():
        setattr(self, key, value)
