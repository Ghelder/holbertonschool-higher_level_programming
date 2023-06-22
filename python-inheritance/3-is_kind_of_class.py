#!/usr/bin/python3
"""Declares a function if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
        False otherwise.

    Example:
        >>> is_kind_of_class(3, int)
        True
        >>> is_kind_of_class('hello', int)
        False
    """
    return isinstance(obj, a_class)
