#!/usr/bin/python3
""" task 6 """
class Square:
    """ class Square that defines a square """
    
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def size(self):
        return self.__size

    def position(self):
        return self.__position

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
                raise TypeError(str)
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
