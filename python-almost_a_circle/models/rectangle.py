#!/usr/bin/python3
""" task 2 """

from models.base import Base

class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width = width of rectangle
        height = height of rectangle
        x = position x of rectangle
        y = position y of rectangle
        id = identifier of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for n in range (self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method so that it returns ...
        """
        return(f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    
    def display(self):
        """
        print in stdout the Rectangle instance with the character # by taking care of x and y
        """
        for n in range (self.y):
            print("")
        for n in range (self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
