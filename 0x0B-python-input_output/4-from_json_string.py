#!/usr/bin/python3
"""
contains from_json_string module
"""


import json


def from_json_string(my_str):
    """ returns an obj repr by a JSON string"""
    return json.loads(my_str)
