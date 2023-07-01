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
