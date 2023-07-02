#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialice
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for n, e in kwargs.items():
                setattr(self, n, e)
