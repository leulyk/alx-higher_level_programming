#!/usr/bin/python3

"""
    Rectangle class for the 'Almost a Circle' project
"""
from models.base import Base


class Rectangle(Base):
    """ a class representing a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for the rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x-coordinate of starting point of the rectangle
            y: y-coordinate of starting point of the rectangle
            id: id of the Rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for the width private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width private instance attribute """
        self.__check(value, 1, 'width')
        self.__width = value

    @property
    def height(self):
        """ getter for the height private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height private instance attribute """
        self.__check(value, 1, 'height')
        self.__height = value

    @property
    def x(self):
        """ getter for the x private instance attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for the x private instance attribute """
        self.__check(value, 0, 'x')
        self.__x = value

    @property
    def y(self):
        """ getter for the y private instance attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for the y private instance attribute """
        self.__check(value, 0, 'y')
        self.__y = value

    def __check(self, value, limit, attrib):
        """ validator of attribute
        Args:
            value: the value to check
            limit: lower limit of the value to check
            attrib: name of the attribute
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attrib))
        if value < limit:
            raise ValueError("{} must be {} 0".format(attrib, ">=" if
                                                      limit == 0 else ">"))

    def area(self):
        """ compute area of a Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ displays a rectangle using # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" "*self.__x, "#"*self.__width))

    def __str__(self):
        """ string representation of a Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ update id, dimension or coordinate of a Rectangle instance """
        if args and args != []:
            keys = list(self.__dict__)
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary representation of a Rectangle instance """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
