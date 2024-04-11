#!/usr/bin/python3
"""Definees."""


class Rectangle:
    """Repreangle."""

    def __init__(self, width=0, height=0):
        """Initiaangle.

        Args:
            width (int): The widectangle.
            height (int): The heigectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gsetangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ctangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return ngle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Retur Rectangle.

        Representcharacter.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for k in range(self.__height):
            [r.append('#') for h in range(self.__width)]
            if k != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Reture Rectangle."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """Printectangle."""
        print("Bye rectangle...")
