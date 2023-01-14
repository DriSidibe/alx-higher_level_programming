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

    def to_json_string(list_dictionaries):
        if list_dictionaries in [None, []]:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open("Rectangle.json", "w") as file:
            file.write(to_json_string(map(lambda obj : obj.to_dictionary(), list_objs)))
