#!/usr/bin/python3
"""Define a lookup function which returns a list of objects.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
