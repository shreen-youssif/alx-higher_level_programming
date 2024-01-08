#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """MyInt class inherits int class"""

    def __eq__(self, other):
        """check if other is not equal to the object

        :param other: the object to compare with

        :return: False if object is equal to other
        otherwise True
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """check if other is equal to the object

        :param other: the object to compare with

        :return: True if object is equal to other
        otherwise False
        """
        return super().__eq__(other)
