#!/usr/bin/python3
"""
contains class Student
"""


class Student:
    """initialize attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """retrieve a dict repr of student"""
    def to_json(self):
        return self.__dict__
