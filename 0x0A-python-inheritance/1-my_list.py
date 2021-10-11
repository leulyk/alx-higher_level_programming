#!/usr/bin/python3

"""
    module to learn inheritance in python
"""


class MyList(list):
    """ a class that inherits from list """
    def print_sorted(self):
        """ print the list sorted """
        print(sorted(self))
