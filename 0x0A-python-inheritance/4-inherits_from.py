#!/usr/bin/python3
"""Function checking inheritance of an object"""


def inherits_from(obj, a_class):
    """
    check if obj is subclass of a_class
    :param obj: the object to be checked
    :param a_class: the class to compare with
    :return:
        True: if obj is subclass of a_class
        otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
