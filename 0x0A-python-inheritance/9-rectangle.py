#!/usr/bin/python3
"""
contains class BaseGeometry and subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initialize class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """informal str rep of the rect"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
