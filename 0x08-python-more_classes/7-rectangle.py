#!/usr/bin/python3
"""Definlass."""


class Rectangle:
    """Represenangle.

    Attributes:
        n (int): The numnstances.
        print_symbol (any): Thepresentation.
    """

    n = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialngle.

        Args:
            width (int): The wiectangle.
            height (int): The heighngle.
        """
        type(self).n += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getectangle."""
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
        """Get the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returntangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returion oectangle.

        Represe # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a messagangle."""
        type(self).n -= 1
        print("Bye rectangle...")
