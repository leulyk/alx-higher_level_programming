#!/usr/bin/python3

"""
    Project on python classes and objects
    Rectangle class #9
"""


class Rectangle:
    """ A class representing a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ compute area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ compute perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ string representation of the rectangle class """
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            for j in range(self.__width):
                output += str(self.print_symbol)
            if i != self.__height - 1:
                output += "\n"
        return output

    def __repr__(self):
        """ returns string representation of the rectangle to be
            able to recreate a new instance by using eval() """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
            + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ class method to define a rectangle with the same width and
            height
        """
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size < 0:
            raise ValueError('width must be >= 0')
        return Rectangle(size, size)
