#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    for i in new_list:
        if idx < 0 and idx > len(new_list):
            return new_list
        else:
            new_list.pop(idx)
            new_list.insert(idx, element)
            return new_list
