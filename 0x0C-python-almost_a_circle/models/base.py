#!/usr/bin/python3
"""Basic class Base"""
from json import dumps, loads


class Base:
    """the base class for all other classes called Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        '''dumps list of dictionaries into json string'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
