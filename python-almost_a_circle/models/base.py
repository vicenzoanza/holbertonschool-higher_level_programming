#!/usr/bin/python3
""" task 1 """
class Base:
""" class base

__nb_objects = Is the counter of objects


"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize
        id = identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
