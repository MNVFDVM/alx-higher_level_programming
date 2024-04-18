#!/usr/bin/python3

"""Defineerferf erfrefer fref refrefre frefereometry."""


class BaseGeometry:
    """Reprsrerfer frefer frefre ry."""

    def area(self):
        """Noteffer erfrefre frefted."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validfe fewrfref erferfer fteger.
        Args:
            name (str): The naregf efffr remeter.
            value (int): Theergtr gtrgtrg trgtridate.
        Raises:
            TypeError: If valufcfeffr efref ger.
            ValueError: If dfedf fefrefre f0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
