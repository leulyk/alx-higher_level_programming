#!/usr/bin/python3

"""
    Python I/O Project, Task 8
"""

import json


def class_to_json(obj):
    """ return the dictionary description with simple data
        structure for JSON serialization of an object
    """
    return obj.__dict__
