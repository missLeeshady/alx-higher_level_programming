#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new = list(my_list)
    for item in new:
        if item % 2 == 0:
            new[item] = True
        else:
            new[item] = False
    return new
