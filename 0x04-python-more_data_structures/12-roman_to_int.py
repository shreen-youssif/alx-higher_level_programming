#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    total = 0
    number = 0
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for char in reversed(roman_string):
        number = roman_dict[char]
        total += number if total < number else -num
    return total
