#!/usr/bin/python3

"""
    Module for the base class of the 'Almost a Circle' project
"""

import json
import csv


class Base:
    """ Base class for all other classes in the project whose aim is to
        manage id attribute of all future classes and avoid duplicates
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for the base class
        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string representation of a list of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_obj):
        """ writes a JSON string representation of a list of objects """
        new_list = []
        with open("{}.json".format(cls.__name__), "w") as file:
            for obj in list_obj:
                new_list.append(obj.to_dictionary())
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of dictionaries from a json string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns list of instances from file """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, mode="r", encoding='utf-8') as file:
                file_output = file.read().replace("\'", '\"')
                dictionaries = cls.from_json_string(file_output)
                instances = []
                for dictionary in dictionaries:
                    instances.append(cls.create(**dictionary))
                return instances
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """ returns list of instances from file """
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=',',
                                    lineterminator='\n')
                if file_name == "Rectangle.csv":
                    columns = ['id', 'width', 'height', 'x', 'y']
                else:
                    columns = ['id', 'size', 'x', 'y']
                instances = []
                for row in reader:
                    dictionary = {}
                    count = 0
                    for i in row:
                        dictionary[columns[count]] = int(i)
                        count += 1
                    instances.append(cls.create(**dictionary))
                return instances
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_obj):
        """ writes a CSV reprentation of a list of objects to a file """
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8") as file:
            if file_name == "Rectangle.csv":
                columns = ['id', 'width', 'height', 'x', 'y']
            else:
                columns = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(file, fieldnames=columns, delimiter=",",
                                    lineterminator="\n")
            for obj in list_obj:
                writer.writerow(obj.to_dictionary())
