#!/usr/bin/python3
""" Module for is_kind_of_class method"""


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        Method that raises an Exception with message area() is not implemented
        """
        raise Exception("area() is not implemented")
