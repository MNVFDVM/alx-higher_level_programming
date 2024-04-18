#!/usr/bin/python3

"""Defdfgr gtrgtr gtrg trgtr gtrg trgtrg trgtrg trgtrtgtry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprdsf rfrefer frefre feometry."""

    def __init__(self, width, height):
        """Intialdfer frefer frefle.
        Args:
            width (int): The wirefer referf refre ftangle.
            height (int): The heidsfr fedferf erftangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
