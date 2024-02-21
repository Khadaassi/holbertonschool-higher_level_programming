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
        """
        Method that prints in stdout the Rectangle
        instance with the character #
        """
        if self.height == 0 or self.width == 0:
            print()
        else:
            for _ in range(self.y):
                print()
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns:
            str: A string in the format "[Class Name] (id) x/y - width/height".
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.__width,
            self.__height,
        )

    def update(self, *args, **kwargs):
        """
        Updates the class Rectangle by assigning an argument to each attribute.
        Args:
            *args: Variable-length positional args for id, width, height, x, y.
            **kwargs: Keyword arguments for id, width, height, x, and y.
        """
        if args:
            attributs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributs):
                    setattr(self, attributs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        Returns:
            dict: A dictionary containing the id, width, height, x, and y.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
