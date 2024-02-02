#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    old_one = a_dictionary
    new_dictionary = {key: old_one[key] * 2 for key in sorted(old_one)}
    return new_dictionary
