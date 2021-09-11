#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxint = 0
    for i in my_list:
        if i > maxint:
            maxint = i
    return maxint
