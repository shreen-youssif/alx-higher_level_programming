#!/usr/bin/python3
'''Module for Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Informal string representaion of square'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __modify(self, id=None, size=None, x=None, y=None):
        '''modify square attributes by args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''modify square attributes by keywords'''
        if args:
            self.__modify(*args)
        elif kwargs:
            self.__modify(**kwargs)

    def to_dictionary(self):
        '''display the square info as dictionary'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
