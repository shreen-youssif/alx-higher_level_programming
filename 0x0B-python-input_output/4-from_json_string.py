#!/usr/bin/python3
"""JSON representation of Data Structure"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
