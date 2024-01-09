#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """Returns the dictionary description with a simple data structure
    for JSON serialization of an object
    """

    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        for key, value in result.items():
            if hasattr(value, "__dict__"):
                result[key] = class_to_json(value)
        return result
    return obj
