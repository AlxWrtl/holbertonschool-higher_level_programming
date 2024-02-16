class Student:
    """A class to represent a student with customizable attributes.

    This class defines a Student with first name, last name, and age attributes.
    It includes a method to serialize the student instance into a dictionary,
    optionally filtering and ordering the serialized data based on specific
    attributes.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
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

    def to_json(self, attrs=None):
        """Serialize the student instance into a dictionary.

        Optionally filters and orders the serialized data based on specific
        attributes if provided. If `attrs` is a list, only attributes included
        in `attrs` are serialized. Additionally, attempts to order the
        serialized data based on a preferred order.

        Args:
            attrs (list, optional): A list of attribute names to be included in
                                    the serialized dictionary. If None, all
                                    attributes are included.

        Returns:
            dict: A dictionary representation of the Student instance,
            filtered and ordered as specified.
        """
        result_dict = {}
        if isinstance(attrs, list):
            attributes = {key: getattr(self, key)
                for key in attrs if hasattr(self, key)}
        else:
            attributes = self.__dict__
        preferred_order = ['age', 'last_name', 'first_name']
        for key in preferred_order:
            if key in attributes:
                result_dict[key] = attributes.pop(key)
        for key in sorted(attributes.keys()):
            result_dict[key] = attributes[key]
        return result_dict
