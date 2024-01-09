#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends text to a file

    Args:
        filename (str): file name
        text (str): text to be added to file
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
