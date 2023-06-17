#!/usr/bin/python3
"""defines a square class"""


class Square:
    """square class with private attribute instance
    Attributes:
        __size: instance private attribute
    """
    def __init__(self, size=0):
        """initializing the instance

        valid:
            size must be an integer
            if size is less than 0

        Args:
            __size: defines the private instance
            size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
