#!/usr/bin/python3
"""Module for Student class definition.

This module defines a Student class with attributes for first name, last name,
and age. It includes functionality to serialize the Student instance into a
JSON-compatible dictionary representation.
"""


class Student:
    """A class to represent a student with personal information.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance.

        Converts the Student instance into a dictionary, making it compatible
        for serialization into JSON format. This is achieved by returning the
        instance's built-in __dict__ attribute.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
