#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for key, value in new.items():
        new[key] = value * 2
    return new
