#!/usr/bin/python3
"""Defines class Student ."""


class Student:
    """Object that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the data

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure

        Args:
            attrs (list): List of attributes

        Returns:
            The dictionary description with simple data structure
        """

        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
