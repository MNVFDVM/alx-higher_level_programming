#!/usr/bin/python3
"""Defineslass."""


class Rectangle:
    """Reprectangle.

    Attributes:
        number_of_instances (int): The numberstances.
        print_symbol (any): The symboesentation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialiangle.

        Args:
            width (int): retgrtctangle.
            height (int): The he newctangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get thwitangle."""
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
        """Get theectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returntharangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retumeterctangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returntreater aea.

        Args:
            rect_1 (Rectangle): The fingle.
            rect_2 (Rectangle): The sectangle.
        Raises:
            TypeError: Ifeitherectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return anewsize.

        Args:
            size (int): The widtRectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """ReturRectangle.

        Representharacter.
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
        """ReturnRectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    def __del__(self):
        """PrintRectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
