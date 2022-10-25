#!/usr/bin/python3
"""
Contains append_write module
"""

def append_write(filename="", text=""):
    """returns number of char written"""
    with open('filename', 'a+', encoding="utf=8") as f:
        return f.write(text)
