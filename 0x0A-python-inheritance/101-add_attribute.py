#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 13
"""


def add_attribute(obj, attr, val):
    """ adds an attribute to an object at runtime """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
