#!/usr/bin/python3

"""
    Python I/O Project, Task 8
"""


def class_to_json(obj):
    """ return the dictionary description with simple data
        structure for JSON serialization of an object
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    return {}
