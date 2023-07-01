#!/usr/bin/python3
"""Definite class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ "Class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            ValueError: If the new size value is negative.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the object.

        Args:
            args: Positional arguments containing the new values for the
            attributes.
            kwargs: Keyword arguments containing the new values for the
            attributes.
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.size = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)
