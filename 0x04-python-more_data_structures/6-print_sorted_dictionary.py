#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, s in sorted(a_dictionary.items(), key=lambda x: x[0]):
        print("{}: {}".format(i, s))
