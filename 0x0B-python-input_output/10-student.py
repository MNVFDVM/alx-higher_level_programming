#!/usr/bin/python3

"""Defingthg trgtgtrg tgtgtrgent."""


class Student:
    """Reprefffr ergrgr rgergrtgent."""

    def __init__(self, first_name, last_name, age):
        """Initialffgtr gtgtr gtrnt.
        Args:
            first_name (str): Thrgtrg fgg gregrgrgr rgrgdent.
            last_name (str): Thertg fgfrrg fgfdg fgfudent.
            age (int): Thtgt rfgtrg trgtrg trent.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gettgg rgrg rgtrgtr gtrgtr gtrgtrgtrnt.
        If attgg fgfrgrfg eg vfvfvvfvfvf vfvfv fvst.
        Args:
            attrs (list): erf erferf erfref erferf erfent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
