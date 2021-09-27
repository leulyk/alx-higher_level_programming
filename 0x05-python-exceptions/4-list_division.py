#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(list_length):
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except Exception as e:
            if isinstance(e, ValueError) or isinstance(e, TypeError):
                print("wrong type")
            if isinstance(e, ZeroDivisionError):
                print("division by zero")
            if isinstance(e, IndexError):
                print("out of range")
            quotient = 0
        finally:
            result.append(quotient)
    return result
