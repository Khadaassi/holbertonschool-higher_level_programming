#!/usr/bin/python3

"""Module for Rectangle class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle:
    """This is a class for a rectangle."""

    def __init__(self, width, height):
        """The constructor for Rectangle class."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """This method returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
