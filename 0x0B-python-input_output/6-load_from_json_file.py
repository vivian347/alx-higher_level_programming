#!/usr/bin/python3
"""
contains load_from_json_file module
"""


import json


def load_from_json_file(filename):
    """creates an obj from a json file"""
    with open(filename, 'r', encoding="utf=8") as f:
        return json.load(f)
