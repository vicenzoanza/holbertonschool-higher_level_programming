#!/usr/bin/python3
""" class Square """
class Square:
    """ class Square that defines a square, if size if not int TypeError or size < 0 ValueError """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")


