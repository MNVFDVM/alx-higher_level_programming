#!/usr/bin/python3

"""Deferfer erfre ferfer fre refrre."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprdfgfer erfer ferfre."""

    def __init__(self, size):
        """Inieregfer refer frefer fre.
        Args:
            size (int): Thedfre refref erfref reuare.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
