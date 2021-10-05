#!/usr/bin/python3

"""
    Demonstrates a class that makes it impossible to create
    new instance attributes of it dynamically
"""


class LockedClass:
    """ class that prohibits creation of new instance attributes
        dynamically
    """
    __slots__ = ['first_name']
