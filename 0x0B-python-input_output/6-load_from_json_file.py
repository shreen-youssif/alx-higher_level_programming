#!/usr/bin/python3
"""Creating Object using JSON fil"""
import json


def load_from_json_file(filename):
    """creating obj located inside json file"""
    with open(filename, 'r') as my_file:
        return json.load(my_file)
