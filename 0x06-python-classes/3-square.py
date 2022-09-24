#!/usr/bin/python3

""" Defines a class square"""


class Square:
    """Represents a square

    Attributes:
        __size(int): size of a side 
    """
    def __init__(self, size=0):
        """Initializes the suare
        Args:
            size(int): size of side
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area

        Returns: area
        """
        result = self.__size ** 2
        return result
