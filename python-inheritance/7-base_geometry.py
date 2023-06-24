#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """class BaseGeometry based."""

    def area(self):
        """Method instance area.

        Returns:
            Exception: area() is not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
