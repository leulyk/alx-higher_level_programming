#!/usr/bin/python3

""" Python I/O Project, Task 0 """


def read_file(filename=""):
    """ read from a file """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
