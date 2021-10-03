#!/usr/bin/python3
"""
    Project for learning doctests
    0_add_integer module
"""


def add_integer(a, b=98):
    """ adds two integers
    Args:
        a: first integer
        b: second integer (defaults to 98)
    If arguments are not of integer or float data type, raise
    TypeError
    If floats are provided, casts them to integers
    Returns:
        sum of the two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
