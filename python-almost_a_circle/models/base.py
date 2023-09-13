#!/usr/bin/python3
""" task 1 """
import json


class Base:

    """
    class base

    __nb_objects = Is the counter of objects


    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize
        id = identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def save_to_file(cls, list_objs):
        """  that writes the JSON string representation of list_objs """
        filename = cls.__name__ + ".json"
        objects = []
        if list_objs is not None:
            objects = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w") as file:
            file.write(Base.to_json_string(objects))
