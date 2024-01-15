#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width'''
        return self.__width

    @width.setter
    def width(self, value):
        validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height'''
        return self.__height

    @height.setter
    def height(self, value):
        validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x dimension'''
        return self.__x

    @x.setter
    def x(self, value):
        validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''y dimension'''
        return self.__y

    @y.setter
    def y(self, value):
        validation("y", value)
        self.__y = value

    def validation(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Calculate the area of this rectangle'''
        return self.width * self.height

    def display(self):
        '''display '''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Informal string represnetation of rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(self.id, self.x, self.y, self.width, self.height)

    def __modify(self, id=None, width=None, height=None, x=None, y=None):
        '''modify the rectangle attributes'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update rectangle attributes by args and keywords'''
        # print(args, kwargs)
        if args:
            self.__modify(*args)
        elif kwargs:
            self.__modify(**kwargs)
