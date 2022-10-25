#!/usr/bin/python3
"""
Contains to_json_string module
"""


import json


def to_json_string(my_obj):
    """returns JSON rep of an object"""
    return json.dumps(my_obj)
