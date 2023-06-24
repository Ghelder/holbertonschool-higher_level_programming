#!/usr/bin/python3
"""Defines a function retrun the JSON representation of an object."""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to convert.

    Returns:
        The JSON representation of an object (string)."""

    return json.loads(my_str)
