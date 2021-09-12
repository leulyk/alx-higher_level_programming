#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        separator = ""
        for col in row:
            print("{:s}{:d}".format(separator, col), end="")
            separator = " "
        print()
