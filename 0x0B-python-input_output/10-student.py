#!/usr/bin/python3

"""
    Python I/O Project, Task 10
"""


class Student:
    """ a class representing a student """
    def __init__(self, first_name, last_name, age):
        """ constructor of Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of Student class """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            dct = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dct[key] = self.__dict__[key]
            return dct
        else:
            return self.__dict__
