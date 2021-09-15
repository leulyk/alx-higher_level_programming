#!/usr/bin/python3


def square_matrix_simple(matrix=[[]]):
    squared = []
    for row in matrix:
        squared.append(list(map(lambda x: x * x, row)))
    return squared
