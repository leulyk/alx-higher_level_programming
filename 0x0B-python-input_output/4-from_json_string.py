#!/usr/bin/python3

""" Python I/O Project, Task 4 """

import json


def from_json_string(my_str):
    """ returns object represented by a JSON string """
    return json.loads(my_str)
