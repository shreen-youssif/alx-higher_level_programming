#!/usr/bin/python3
"""Defines Function to add aAttribute to an object if possible"""


def add_attribute(obj, attr, value):
    """
    addition of not previous present attribute
    :param obj(any): the Object to add attribute to
    :param attr(str): what we call this attribute
    :param value(any): the value of this attribute

    :raises:
    TypeError: if this attribute already present
    """
    if not hasattr(obj, attr):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
