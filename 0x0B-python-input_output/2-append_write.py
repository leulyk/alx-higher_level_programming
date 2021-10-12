#!/usr/bin/python3

""" Python I/O Project, Task 2 """


def append_write(filename="", text=""):
    """ append a text to a file """
    with open(filename, "a", encoding="utf-8") as f:
        nc = f.write(text)
        return nc
