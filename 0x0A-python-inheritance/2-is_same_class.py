#!/usr/bin/python3
"""
contains is_same function
"""


def is_same_class(obj, a_class):
    """check if obj of the same class as a_class or not
        Args:
            obj(any): the object
            a-class(class): the class
        Returns:
            True: if object is the same class as a_class
            False: if not
    """
    if not isinstance(obj, a_class):
        return False
    return True
