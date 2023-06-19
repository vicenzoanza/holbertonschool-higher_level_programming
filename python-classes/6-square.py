#!/usr/bin/python3
""" Task 6 """
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        if not check_positive_tuple(value) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print()

            for i in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()
