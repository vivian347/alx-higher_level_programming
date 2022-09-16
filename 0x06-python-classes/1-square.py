#!/usr/bin/python3

"""class Square that defines a square with private attr size"""

class Square:
    """ a class Square"""

    """initializing the attribute size"""
    def __init__(self, size):
        """creating attribute size which is private"""
        self.__size = size
