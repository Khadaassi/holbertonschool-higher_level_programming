#!/usr/bin/python3

"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    __size: size of the square
    __x: x coordinate of the square
    __y: y coordinate of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the square
        """

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square
        """

        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Dictionary representation of the square
        """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
