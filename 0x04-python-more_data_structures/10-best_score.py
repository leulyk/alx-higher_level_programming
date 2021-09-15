#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        i = 0
        for key in a_dictionary.keys():
            if i == 0 or a_dictionary[key] > maxval:
                topkey = key
                maxval = a_dictionary[key]
            i += 1
        return topkey
    return None
