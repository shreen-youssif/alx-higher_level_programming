#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """Defines MyList class that inherits list class"""

    def __int__(self):
        """Initialize MyList object"""
        super().__init__()

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
