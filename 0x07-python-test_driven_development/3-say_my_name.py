#!/usr/bin/python3
"""
3-say_my_name module

It calls a fn thet prints your first and last name
"""


def say_my_name(first_name, last_name=""):
    """ It prnts 'my name is' followed by either 1 or 2 names """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
