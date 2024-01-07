#!/usr/bin/python3
"""Defines an addition function"""


def add_integer(a, b=98):
    """Return the result of addition of two integers
    float arguments converted into integers

    Raises:
        TypeError: if a or b are not integers or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

