#!/usr/bin/python3
""" task 8 """
class Rectangle:
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
