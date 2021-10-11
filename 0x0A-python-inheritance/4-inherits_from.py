#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 4
"""


def inherits_from(obj, a_class):
    """ check whether an object inherits from a class """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
