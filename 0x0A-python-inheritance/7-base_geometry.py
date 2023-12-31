#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value is integer and greater than 0
        Args
            name(string): name of the object
            value: the value to be validated
        Raises:
            TypeError: if value not integer
            ValueError: if value is less or equal to 0
        Return:
            True if value is integer and greater than 0
            otherwise False
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
