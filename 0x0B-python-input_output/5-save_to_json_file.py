#!/usr/bin/python3
"""
contains save_to_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text fileusing json repr"""
    with open(filename, 'w', encoding='utf=8') as f:
        json.dump(my_obj, f)
