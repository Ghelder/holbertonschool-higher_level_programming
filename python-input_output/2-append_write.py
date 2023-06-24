#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""

def append_write(filename="", text=""):
    """Prints the contents of a text file.

    Args:
        filename (str): The name of the file to write to.
    Returns the number of characters written.
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
