#!/usr/bin/python3
"""
contains class BaseGeometry
"""

class BaseGeometry:
    """ contains public attrs area and integer_validation"""
    def area(self):
        """raises an exception area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise a TypeError if val != int"""
        if (type(value) != int):
            raise TypeError("{:d} must be an integer".format(name))
        """raise a ValueError if value <= 0"""
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
