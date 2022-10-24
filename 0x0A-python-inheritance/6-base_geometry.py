#!/usr/bin/python3
"""
contains module area
"""

class BaseGeometry:
    """class with public attr area"""
    def area(self):
        """ raises exception when called """
        raise Exception("area() is not implemented")
