#!/usr/bin/python3
"""JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Give json representation an obj

    :arg
        my_obj: the object to give to json
    """
    return json.dumps(my_obj)
