#!/usr/bin/python3
"""square class definition"""


class Square:
    """square class with private attribute instance
    Attributes:
        __size: instance private attribute
    """

    def __init__(self, size=0):
        """initializing the instance

        Args:
            __size: defines the private instance
            size(int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """The get method returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """valid:
            size must be an integer
            if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public method calculate the square area
        Returns:
            square area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
