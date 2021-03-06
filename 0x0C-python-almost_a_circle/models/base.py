#!/usr/bin/python3
"""This module contains a class called Base"""


class Base():
    """
        This class will be the “base” of all other
        classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: list of dictionaries
        """
        import json

        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs
        to a file.

        Args:
            list_objs: is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + '.json'

        with open(file_name, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dict = []
                for i in list_objs:
                    list_dict.append(i.to_dictionary())

                f.write(i.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        json_string.

        Args:
            json_string json string: json string representation
            of a list.
        """
        import json
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes
        already set.
        """
        from models.square import Square
        from models.rectangle import Rectangle
        if 'size' in dictionary:
            new_inst = Square(size=1)
        elif 'width' in dictionary:
            new_inst = Rectangle(width=1, height=1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        import json
        new_list = []
        file_name = cls.__name__ + '.json'

        try:
            with open(file_name, "r", encoding="utf-8") as f:
                json_ret = f.read()
        except Exception:
            return new_list

        ret = cls.from_json_string(json_ret)

        for i in ret:
            r = cls.create(**i)
            new_list.append(r)

        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """that writes the JSON string representation of list_objs
        to a file.

        Args:
            list_objs: is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + '.csv'

        with open(file_name, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dict = []
                for i in list_objs:
                    list_dict.append(i.to_dictionary())

                f.write(i.to_json_string(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances."""
        import json
        new_list = []
        file_name = cls.__name__ + '.csv'

        try:
            with open(file_name, "r", encoding="utf-8") as f:
                json_ret = f.read()
        except Exception:
            return new_list

        ret = cls.from_json_string(json_ret)

        for i in ret:
            r = cls.create(**i)
            new_list.append(r)

        return new_list
