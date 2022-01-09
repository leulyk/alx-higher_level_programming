#!/usr/bin/python3

"""
    Interview preparation exercise
    -- Algorithm must have lowest complexity
"""


def find_peak(list_int):
    """ find the peak in a list of integers """
    if list_int == []:
        return None
    elif len(list_int) == 1:
        return list_int[0]
    elif len(list_int) == 2:
        return list_int[0] if list_int[0] > list_int[1] else list_int[1]
    else:
        for i in range(1, (len(list_int) + 1) // 2):
            back = len(list_int) - i - 1
            if list_int[i] >= list_int[i - 1] and \
               list_int[i] >= list_int[i + 1]:
                return list_int[i]
            elif list_int[back] >= list_int[back - 1] and list_int[back] >= \
                    list_int[back + 1]:
                return list_int[back]
    return None
