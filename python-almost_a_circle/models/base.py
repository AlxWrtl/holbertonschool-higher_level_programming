#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            self.id = self.increment_objects_count()

    @classmethod
    def increment_objects_count(cls):
        cls.__nb_objects += 1
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def from_json_string(json_string):
        list_dicts = []
        if json_string is not None:
            for obj in json_string:
                list_dicts.append(obj.to_dictionary())
        return json_string
