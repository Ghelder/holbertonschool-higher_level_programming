#!/usr/bin/python3
"""defines a square class"""


class Square:
    """square class with private attribute instance
    Attributes:
        __size: instance private attribute
    """
    def __init__(self, size):
        """initializing the instance
        Args:
            __size: defines the private instance
        """
        self.__size = size
