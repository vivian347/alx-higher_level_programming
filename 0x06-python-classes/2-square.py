#!/usr/bin/python3

"""defining a class Square"""


class Square:
    """Represents a square

    Attributes:
    __size(int): size of a side of a square
    """
    def __init__(self, size=0):
        """creating instance of size
        Args:
            size(int): size of a side of a square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
