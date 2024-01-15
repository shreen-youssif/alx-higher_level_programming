#!/usr/bin/python3
"""Basic class Base"""


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
