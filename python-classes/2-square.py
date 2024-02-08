#!/usr/bin/python3

"""class Square that defines a square"""


class Square:

    """ Square class that define a square with is size"""

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """square size private instance attribute"""
        self.__size = size
