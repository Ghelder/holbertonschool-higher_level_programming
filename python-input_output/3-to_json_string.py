#!/usr/bin/python3
"""Defines a function return the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to convert.

    Returns:
        The JSON representation of an object (string)."""

    return json.dumps(my_obj)
