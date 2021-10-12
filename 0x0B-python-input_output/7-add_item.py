#!/usr/bin/python3

""" Python I/O Project, Task 7 """

from sys import argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    if exists("add_item.json"):
        ls = load_from_json_file("add_item.json")
    else:
        ls = []
    for i in range(1, len(argv)):
        ls.append(argv[i])
    save_to_json_file(ls, "add_item.json")
