#!/usr/bin/python3
"""Defines a function that writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Prints the contents of a text file."""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
