#!/usr/bin/python3
""" defines a class square """


class Square:
    """ Reresents a square
    Attributes:
        __size (int): size of sides f the square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size

    def area(self):
        """ Calculates the area

        Returns: area
        """
        return (self.__size) ** 2

    def my_print(self):
        """Prints the square

        Returns: None
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of side

        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=")
        else:
            self.__size = value
