#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the side
    """
    def __init__(self, size=0):
        """ initialize the class
        Args:
            size(int): size of sides of square
        Returns:
            None
        """
        self.size = size
    def area(self):
        return (self.__size)** 2
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
