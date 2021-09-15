#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    num = den = 0
    for tpl in my_list:
        i, j = tpl
        num += (i * j)
        den += j
    return num / den
