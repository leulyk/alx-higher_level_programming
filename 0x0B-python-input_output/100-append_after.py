#!/usr/bin/python3

""" Append a line in a specified location in a file """


def append_after(filename="", search_string="", new_string=""):
    """ appends a string after each line containing a specific string """
    input_list = output_list = []
    with open(filename, "r") as f:
        input_list = f.readlines()

    for line in input_list:
        output_list.append(line)
        if search_string in line:
            output_list.append(new_string)

    with open(filename, "w") as f:
        f.writelines(output_list)
