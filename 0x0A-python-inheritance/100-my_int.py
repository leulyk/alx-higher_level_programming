#!/usr/bin/python3

"""
    0x0A. Python - Inheritance, Task 12
"""


class MyInt(int):
    """ class that inherits from int and inverts
        the == and != operators
    """
    def __eq__(self, other):
        """
            == operator, return !=
        """
        return super().__ne__(other)
        # return int(self) != int(other)

    def __ne__(self, other):
        """
            != operator, return ==
        """
        return super().__eq__(other)
        # return int(self) == int(other)
