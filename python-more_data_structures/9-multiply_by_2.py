#!/usr/bin/python3
def multiply_by_2(a_dictionary):


    new_dictionary = {key: a_dictionary[key] * 2 for key in sorted(a_dictionary)}
    return new_dictionary
