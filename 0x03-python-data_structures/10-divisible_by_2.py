#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for i in my_list:
            new_list.append(False if i % 2 else True)
    return new_list
