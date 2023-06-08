#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mult = []
    for i in my_list:
        if i % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return mult
