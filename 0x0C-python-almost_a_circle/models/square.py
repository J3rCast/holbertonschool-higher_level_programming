#!/usr/bin/python3
"""This module contains a class called
Square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a Square
    and inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method

        Args:
            size (int): size of the square

            x (int, optional): when display method is called
            prints the square based on axis x. Defaults to 0.

            y (int, optional): when display method is called
            prints the square based on axis y. Defaults to 0.

            id (int, optional): if id is not define it will
            automatically be assign. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size.

        Args:
            value (int): new value of the size.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """override the str magic method

        Returns:
            string to print when print function is used.
        """
        ret = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
        return ret

    def update(self, *args, **kwargs):
        """This method update the attributes."""
        if args:
            i = 0
            for arg in args:
                if len(args) > 1 and i == 1:
                    self.__dict__[list(self.__dict__)[i]] = arg
                    i += 1
                self.__dict__[list(self.__dict__)[i]] = arg
                i += 1
        elif kwargs:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs[arg]
                if arg == 'size':
                    self.width = kwargs[arg]
                    self.height = kwargs[arg]
                if arg == 'x':
                    self.x = kwargs[arg]
                if arg == 'y':
                    self.y = kwargs[arg]

    def to_dictionary(self):
        """""Return the dictionary representation of
        Square."""""
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['x'] = self.x
        new_dict['size'] = self.width
        new_dict['y'] = self.y
        return new_dict
