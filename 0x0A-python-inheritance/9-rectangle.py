#!/usr/bin/python3

"""Deffre frefref refre frefre frefer  referf ometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rrergrefre ffrfre refer eometry."""

    def __init__(self, width, height):
        """Intisdfef dfre fregle.
        Args:
            width (int): The wierfref erfre fref gle.
            height (int): The herretr gfergfre gregrangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Retuergtr rgtr gftrg trgtrgtr gtgtrge."""
        return self.__width * self.__height

    def __str__(self):
        """Returfre erfer ferf erferfre referfre ferfref er erferngle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string 
