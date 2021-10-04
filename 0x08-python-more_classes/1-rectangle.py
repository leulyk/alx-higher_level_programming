#!/usr/bin/python3

"""
    Project on python classes and objects
    Rectangle class #1
"""


class Rectangle:
    """ A class representing a rectangle """
    def __init__(self, width=0, height=0):
        """ constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter method for width private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width private instance attribute """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter method for height private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height private instance attribute """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
