#!/usr/bin/python3

"""Deftgr grgr rgrgnt."""


class Student:
    """Repvvv vfvrgv grfgrgent."""

    def __init__(self, first_name, last_name, age):
        """Inittergt grgr rgrg regdent.
        Args:
            first_name (str): Thyhty hyth yhy hyhudent.
            last_name (str): Thergr trgrg grgrg grdent.
            age (int): Thegtrg rgtrgtr gtrgtr gtrgnt.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gethgtr rgreergrg rgrgrgrg rgrgrg rgtudent.
        If attrs isibute efref rfref erferf refref erfrefs
        inerfre dfrfr rfist.
        Args:
            attrs (list): gtgtrg rgrfre refer referf referfrefnt.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """gr rgrgrggr rrrg rggr rgrt.
        Args:
            json (dict): The kergtr ffgrgrtg rtgtrgrt gtgtrg trgith.
        """
        for k, v in json.items():
            setattr(self, k, v)
