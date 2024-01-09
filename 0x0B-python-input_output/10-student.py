#!/usr/bin/python3
"""Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student instance with first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instanc"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
