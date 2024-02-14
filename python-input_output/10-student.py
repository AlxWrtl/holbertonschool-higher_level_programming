class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
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
