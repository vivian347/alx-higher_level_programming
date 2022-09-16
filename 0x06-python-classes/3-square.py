#!/usr/bin/python3

""" create a class square"""
class Square:
    def __init__(self, size=0):
        """ create instance of class Square"""
        if type(size) is not int:
            """ if size is not an integer raise an error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ if size < 0 raise error """
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ get area of the square """
        result = self.__size ** 2
        return result
