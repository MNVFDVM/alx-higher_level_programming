#!/usr/bin/python3

"""ertregr erferfre refrefuare."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rregr rgfreg re."""

    def __init__(self, size):
        """Inittrgtr trgtrgt trge.
        Args:
            size (int): The sizrfer frfre ferefrfrfre.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
