#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 6
"""


class BaseGeometry:
    """ a class representing geometry """
    def area(self):
        """ an unimplemented public instance method that
            raises an exception when called
        """
        raise Exception('area() is not implemented')
