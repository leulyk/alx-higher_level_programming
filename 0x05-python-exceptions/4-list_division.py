#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(list_length):
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by zero")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result.append(quotient)
    return result
