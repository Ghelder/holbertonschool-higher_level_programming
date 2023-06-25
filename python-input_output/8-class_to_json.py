#!/usr/bin/python3
"""Define function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
