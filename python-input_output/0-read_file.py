#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Prints the contents of a text file."""
    with open(filename, "r") as f:
        print(f.read(), end="")
