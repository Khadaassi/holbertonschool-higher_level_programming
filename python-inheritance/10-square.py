#!/usr/bin/python3

"""Square class that inherits from Rectangle."""

Rectangle = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """This is a class for a square."""

    def __init__(self, size):
        """The constructor for Square object.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This method returns the area of the square."""
        return self.__size**2

    def __str__(self):
        """
        This method returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
