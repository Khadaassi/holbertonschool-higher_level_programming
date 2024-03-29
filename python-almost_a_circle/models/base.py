#!/usr/bin/python3
"""Base class for all models in the project"""


class Base:
    """
    Base class for all models in the project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
