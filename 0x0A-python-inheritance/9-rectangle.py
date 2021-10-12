#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 9
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class representing a rectangle deriving from BaseGeometry """
    def __init__(self, width, height):
        """ constructor for the Rectangle class """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ compute the area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation of the Rectangle class """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
