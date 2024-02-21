#!/usr/bin/python3

"""Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    __width: width of the rectangle
    __height: height of the rectangle
    __x: x coordinate of the rectangle
    __y: y coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the rectangle class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


def area(self):
    """
    Return the area of the rectangle
    """
    return self.__width * self.__height


def display(self):
    """Prints the rectangle using '#' char in standard output (stdout).
    If either the height or width is 0, it prints an empty line.
    """
    if self.height == 0 or self.width == 0:
        print()
    else:
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)


def __str__(self):
    """ "Returns a string representation of the rectangle.
    Returns:
        str: A string in the format "[Class Name] (id) x/y - width/height".
    """
    return "[{}] ({}) {}/{} - {}/{}".format(
        self.__class__.__name__, self.id, self.x, self.y,
        self.__width, self.__height
    )
