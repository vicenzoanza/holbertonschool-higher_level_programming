#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" task 8 """
class Rectangle:
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
