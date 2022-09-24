#!/usr/bin/python3
""" defining a class square """


class Square:
    """ Represents a square
    Attributes:
        __size (int): size of sides f the square
        __position (tuple): position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the class square
        Args:
            size (int): size of side
            position (tuple): position of square in 2D space
        Returns: None
        """
        self.size = size
        self.position = position

    def area(self):
        """ calculates area of square
        Returns: area
        """
        return (self.__size) ** 2

    def my_print(self):
        """ prints the square
        Returns: none
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
        """ getter of __size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of __size
        Args:
            value (int): size of side
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter of __position
        Returns: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter of __position
        Args:
            value (int):
                position of square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[0]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
