#!/usr/bin/python3
""" base.py """


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
