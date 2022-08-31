#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list[:] = [x if x != search else replace for x in new_list]
    return new_list
