#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            pass
        elif idx > len(my_list):
            pass
        else:
            return my_list[idx]
