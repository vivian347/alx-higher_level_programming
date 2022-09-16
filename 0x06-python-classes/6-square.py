#!/usr/bin/python3

""" creating a class square """
class Square:
    """ instanciate square
    Attributes:
    __size: size of sides f the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
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
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ retrieve position property """
        return self.__position

    @position.setter
    def position(self, value):
        """ set properties of position """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[0]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
