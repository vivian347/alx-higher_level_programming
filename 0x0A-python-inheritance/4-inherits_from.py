#!/usr/bin/python3
"""
Contains the nherits from fun
"""

def inherits_from(obj, a_class):
    """ returs true if obj is a subclass , otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
