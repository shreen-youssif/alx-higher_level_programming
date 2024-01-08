#!/usr/bin/python3
"""Defines Function to add aAttribute to an object if possible"""


def add_attribute(obj, attr, value):
    """
    addition of not previous present attribute
    :param obj: the Object to add attribute to
    :param attr: what we call this attribute
    :param value: the value of this attribute

    :raises:
    TypeError: if this attribute already present
    """
    def add_attribute(obj, attr, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr] = value
