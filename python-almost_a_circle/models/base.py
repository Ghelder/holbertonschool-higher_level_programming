#!/usr/bin/python3
"""Class Base for all other classes"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries."""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file."""
        file_name = f"{cls.__name__}.json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        with open(file_name, "w") as f:
            f.write(cls.to_json_string(obj_list))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
