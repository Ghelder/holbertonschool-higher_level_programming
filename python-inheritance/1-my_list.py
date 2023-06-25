#!/usr/bin/python3
"""Define a class MyList."""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """Prints a sorted list of integers."""
        print(sorted(self))
