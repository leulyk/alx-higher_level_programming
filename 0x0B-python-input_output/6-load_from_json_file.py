#!/usr/bin/python3

""" Python I/O Project, Task 6 """

import json


def load_from_json_file(filename):
    """ load an object from a JSON file """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
