#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): file name
        text (str): text to be add to file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
