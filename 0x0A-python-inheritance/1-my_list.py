#!/usr/bin/python3
""" inherits from list """

class MyList(list):
    def __init__(self):
        """ initialize object """
        super().__init__()

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
