#!/usr/bin/python3
"""Defineclass."""


class Rectangle:
    """Repgle.

    Attributes:
        n (int): The numinstances.
    """

    n = 0

    def __init__(self, width=0, height=0):
        """Initializangle.

        Args:
            width (int): The widew rectangle.
            height (int): The heigctangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Geectangle."""
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
        """tgtrgtrtgngle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returntangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returnctangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Retable represenectangle.

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
        """Return Rectangle."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """Princtangle."""
        type(self).n -= 1
        print("Bye rectangle...")
