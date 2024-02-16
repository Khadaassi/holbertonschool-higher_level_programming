#!/usr/bin/python3

"""Module for Rectangle class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle:
    """This is a class for a rectangle."""

    def __init__(self, width, height):
        """The constructor for Rectangle class."""
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """This method validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """This method returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        This method returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
