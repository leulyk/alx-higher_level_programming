#!/usr/bin/python3

""" Python I/O Projects, Task 1 """


def write_file(filename="", text=""):
    """ write to a file """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
