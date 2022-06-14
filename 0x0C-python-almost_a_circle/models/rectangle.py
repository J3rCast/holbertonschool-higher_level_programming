#!/usr/bin/python3
"""This module contains a class called
Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """This class defines a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constructor method

        Args:
            width : width of the rectangle
            height : height of the rectangel
            x : Defaults to 0.
            y : Defaults to 0.
            id : id of the instance. Defaults to None.
        """
        self.size_validator('width', width)
        self.size_validator('height', height)
        self.axis_validator('x', x)
        self.axis_validator('y', y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def size_validator(name, value):
        """validates the size

        Args:
            name (str): name of the value to validate
            value (int): value to validate

        Raises:
            TypeError: if value is not int
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def axis_validator(name, value):
        """validate the axis

        Args:
            name (str): name of the value to validate
            value (int): vlaue to validate

        Raises:
            TypeError: if value is not int
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """This is getter of the width"""
        return self.__width

    @property
    def height(self):
        """This is getter of the height"""
        return self.__height

    @property
    def x(self):
        """This is getter of the x"""
        return self.__x

    @property
    def y(self):
        """This is getter of the y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter of the width

        Args:
            value (int): New value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter of the height

        Args:
            value (int): New value to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter of x

        Args:
            value (int): New value to set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter of y

        Args:
            value (int): New value to set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__y = value

    def area(self):
        """Method that return the area"""
        result = self.__height * self.__width
        return result

    def display(self):
        """prints a Rectangle based on width and height"""
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return ""
        else:
            [print() for y in range(self.__y)]
            for columns in range(height):
                [print(" ", end="") for x in range(self.__x)]
                for rows in range(width):
                    print("#", end="")
                print()

    def __str__(self):
        """Override str magic method

        Returns:
            String used when print or str is used
        """
        ret = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return ret

    def update(self, *args, **kwargs):
        """This method update the attributes"""
        if args:
            i = 0
            for arg in args:
                self.__dict__[list(self.__dict__)[i]] = arg
                i += 1
        else:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs[arg]
                if arg == 'width':
                    self.__width = kwargs[arg]
                if arg == 'height':
                    self.__height = kwargs[arg]
                if arg == 'x':
                    self.__x = kwargs[arg]
                if arg == 'y':
                    self.__y = kwargs[arg]

    def to_dictionary(self):
        """Return the dictionary representation of
        Rectangle.
        """
        new_dict = {}
        new_dict['x'] = self.__x
        new_dict['y'] = self.__y
        new_dict['id'] = self.id
        new_dict['height'] = self.__height
        new_dict['width'] = self.__width
        return new_dict
