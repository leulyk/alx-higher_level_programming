#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 7
"""


class BaseGeometry:
    """ a class representing geometry """
    def area(self):
        """ an unimplemented public instance method that
            raises an exception when called
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ checks value if it's an integer > 0, and raises
            an exception accordingly
            We can assume name is always a strin
        """
        if not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
