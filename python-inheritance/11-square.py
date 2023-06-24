#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square based on Rectangle."""

    def __init__(self, size):
        """Initialize a new Square."""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Square] {}/{}".format(self.__size, self.__size)
