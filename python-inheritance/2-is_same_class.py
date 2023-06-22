#!/usr/bin/python3
"""This module provides a function to check if an object is exactly an instance
of
a specified class.

Functions:
    is_same_class(obj, a_class):
        Returns True if the object is exactly an instance of the specified
        class.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
        class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare the object's type with.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
        False otherwise."""
    return type(obj) is a_class
