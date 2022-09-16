#!/usr/bin/python3
""" create a class Square """
class Square:
    def __init__(self, size=0):
        """ instantiate the class
        Attributes:
            __size - size of sides of square
        """
        self.size = size
    def area(self):
        """ get area of square """
        return (self.__size)** 2
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """ set value of square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
