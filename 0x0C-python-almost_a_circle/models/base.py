#!/usr/bin/python3

"""Defines model base class"""
import json
import csv
import turtle

class base:
    """Represents the base model
    Representing the base of the almost as a circle
    Attributes:
    __nb_objects (int): The number of installed base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialisez a new base
        Args:
            id (int): The identity of the new base
        """
        if id is not None:
            self.id n= id
        else:
            Base.__nb_objects += 1
            self.id = base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json  list of dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json serilazation of a list of objects to a file
        Args:
            list_objs (list): list of inherited base instances
        """
            filename = cls.__name__+ ".json"
            with open (filename, "w") as jsonfile:
                if list_objs is None:
                    jsonfile.write("[]")
                else:
                    lists_dicts = [o.to_dictionary() for o in list_objs]
                    jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a json string.
        Args:
            json_string (str): json string is a represation of a list of dicts.
        Returns:
            
            if json_string is None or empty which is empty
            otherwise python list represenated by python
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Return json strings from instanced classes
        Reads from '<cls.__name__>.json'
        Returns:
            Empty if the file does not exist
            otherwise, initialized classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r")as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

        @classmethod
        def save_to_file_csv(cls, lists_objs):
            """Write the CSV serialization of list of objects to a file
            Args:
                list_objs (list): list of inherited base instances
            """
            filename = cls.__name__ + ".csv"
            with open(filename, "w", newline="") as csvfile:
                if list_objs is None or list_objs == []:
                    csvfile.write("[]")
                else:
                    if cls.__name__ =="Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    else:
                        fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instatiated in csv file.
        Reads from `<cls.__name__>.csv`
        Returns:
            empty file if the file does not exist
            otherwise, list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict(k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Recatngles and squares using the turtle module
        Args:
            list_rectangles (list): list of reactangle drawn objects
            list_square (list): list of square objects to draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolour("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.colour("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.colour("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle .exitonclick()
