#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 8
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
