#!/usr/bin/python3
"""Square class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a class for a square.
    Args:
        Rectangle (Rectangle): mother class
    """
    def __init__(self, size):
        """
        init a square
        Args:
            size (int): square side size
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        This method returns the area of the square.
        """
        return self.__size ** 2