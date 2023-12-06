#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum_value = 0
    key_1 = ""
    for key , value in a_dictionary.items():
        if value > maximum_value:
            maximum_value = value
            key_1 = key
    return key_1
