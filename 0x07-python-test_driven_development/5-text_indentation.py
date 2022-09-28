#!/usr/bin/python3
"""
the 5-text_indentation mmodule

It calls a fn that prints a text wth 2 new lines after ., ?, :
"""


def text_indentation(text):
    """ function that prints to lines after specified characters """
    matches = [".", "?", ":"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for x in text:
        if flag == 0:
            if x == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if x == '?' or x == '.' or x == ':':
                print(x)
                print()
                flag = 0
            else:
                print(x, end="")
