#!/usr/bin/python3
class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size=0):
        """Initializes the size variable as a private instance attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
    @property
    def size(self):
        """Getter for size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Setter for size"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
