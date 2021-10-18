#!/usr/bin/python3

"""
    Square class for the 'Almost a Circle' project
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class representing a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for a Square instance """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter method for the size private instance attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for the size private instance attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """ string representation of a Square instance """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """ update id, dimension or coordinate of a Square instance """
        if args and args != []:
            arglist = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, arglist[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary representation of a Square instance """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
