#!/usr/bin/python3
"""Class Base for all other classes"""


class Base:
    """Base class for objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class.

        Args:
            id (int, optional): The id of the object. If not provided, a new id
            is assigned.

        Returns:
            None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
