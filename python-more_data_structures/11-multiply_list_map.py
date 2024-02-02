#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    if my_list is None:
        my_list = []
    return list(map(lambda mult: mult * number, my_list))
