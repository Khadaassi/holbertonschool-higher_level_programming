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

    def integer_validator(self, name, value):
        """
        Method that validates value
        """

        if type(value) not in [int]:
            raise TypeError(name + " must be an integer")
            raise TypeError("{} must be an integer".format(name))
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
