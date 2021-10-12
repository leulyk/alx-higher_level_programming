#!/usr/bin/python3

""" Python I/O Project, Task 5 """

import json


def save_to_json_file(my_obj, filename):
    """ save object to json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
