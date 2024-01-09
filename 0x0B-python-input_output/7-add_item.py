#!/usr/bin/python3
""""""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        objects = load_from_json_file("add_item.json")
    except FileNotFoundError:
        objects = []
    objects.extend(sys.argv[1:])
    save_to_json_file(objects, "add_item.json")
