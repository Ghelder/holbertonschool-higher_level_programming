#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and returns it to
stdout."""


def write_file(filename="", text=""):
    """Prints the contents of a text file.

    Args:
        filename (str): The name of the file to write to.
    Returns the number of characters written.
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
