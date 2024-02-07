#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """ Square class that define a square with is size"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square with optional size

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Square position. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):  # get the square size
        return self.__size

    @size.setter
    def size(self, value):  # set the square size

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):  # get the square position
        return self.__position

    @position.setter
    def position(self, value):  # set the square size

        if (
            not isinstance(value, tuple)
            or len(value) != 2 or
            not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
