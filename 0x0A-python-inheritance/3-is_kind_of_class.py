#!/usr/bin/python3
"""check inheritance of a class"""


def is_kind_of_class(obj, a_class):
    """check if obj is subclass of a_class or not
    
    :param obj: the object to be checked
    :param a_class: the class to compare to
    
    :return:
        True: if obj is subclass of a_class
        otherwise false
    """
    if not isinstance(obj, a_class):
        return False
    return True
