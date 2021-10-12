#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 10
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class representing a square deriving from Rectangle """
    def __init__(self, size):
        """ constructor for the Square class """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ compute the area of a square """
        return self.__size * self.__size

    def __str__(self):
        """ string representation of square class """
        return "[Square] {}/{}".format(self.__size, self.__size)
