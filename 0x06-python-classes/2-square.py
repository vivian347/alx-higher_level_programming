#!/usr/bin/python3

"""creating a class Square"""
class Square:
    def __init__(self, size=0):
        """creating instance of size"""
        if type(size) is not int:
            """ check if size is an integer"""
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                """ check if size is less 0 """
                raise ValueError("size must be >= 0")
            else:
                """ else initialize size to be private """
                self.__size = size
