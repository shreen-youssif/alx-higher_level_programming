#!/usr/bin/python3
"""Writting object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Saving obj to text file by using json"""
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
