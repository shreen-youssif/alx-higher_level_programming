#!/usr/bin/python3
"""Basic class Base"""
from json import dumps, loads
import csv


class Base:
    '''Base class all other classes inherits from it'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''dumps list of dictionaries into json string'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''load objects to json file'''
        if list_objs is not None:
            list_objs_d = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs_d))

    @staticmethod
    def from_json_string(json_string):
        '''load json string as dictionary'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create copy of bject similar to the original one'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(5, 5)
        elif cls is Square:
            dummy = Square(5)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Load objects from file to python dictionary'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''dump object to csv'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Load object from file'''
        from models.rectangle import Rectangle
        from models.square import Square
        obj = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                obj.append(cls.create(**d))
        return obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            draw = turtle.Turtle()
            draw.color((randrange(255), randrange(255), randrange(255)))
            draw.pensize(1)
            draw.penup()
            draw.pendown()
            draw.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            draw.pensize(14)
            draw.forward(i.width)
            draw.left(90)
            draw.forward(i.height)
            draw.left(90)
            draw.forward(i.width)
            draw.left(90)
            draw.forward(i.height)
            draw.left(90)
            draw.end_fill()

        time.sleep(10)
