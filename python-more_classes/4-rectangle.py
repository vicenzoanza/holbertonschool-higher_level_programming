#!/usr/bin/python3
""" task 2 """


class Rectangle:
    """Class that defines a rectangle with attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate area rectangle """
        return (self.__width * self.height)

    def perimeter(self):
        """ calculate perimeter rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        alo = ""
        for height in range(self.__height):
            for width in range(self.__width):
                alo += "#"
            if height != self.__height - 1:
                alo += '\n'
        return alo

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
