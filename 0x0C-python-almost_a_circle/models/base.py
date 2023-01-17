#!/usr/bin/python3
""" base.py """

import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries in [None, []]:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("Rectangle.json", "w") as file:
            file.write(cls.to_json_string(list(map(lambda obj : obj.to_dictionary(), list_objs))))

    @staticmethod
    def from_json_string(json_string):
        if json_string in [None, []]:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(5, 5)
        dummy_instance.update(dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        pass
