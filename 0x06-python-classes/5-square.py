#!/usr/bin/python3

""" creating a class square """
class Square:
    """ instanciate square
    Attributes:
    __size: size of sides f the square
    """
    def __init__(self, size=0):
        self.size = size
        """ find area of square """
    def area(self):
        return (self.__size) ** 2
    """ print square using # symbol """
    def my_print(self):
        if self.size == 0:
            """ if size = 0 print a blank line """
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """ retrieve the size property """
        return self.__size

    @size.setter
    def size(self, value):
        """ if value is not an integer raise a TypeError """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            """ if value is < 0 raise a ValueError """
            raise ValueError("size must be >=")
        else:
            """ else set value = __size """
            self.__size = value
