"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/region.html
"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import UnimplementedSikuliClass, SikuliClass
from . import Match

class SikuliEvent(UnimplementedSikuliClass):
    """ Manages interaction with Sikuli's SikuliEvent """
    #TODO: SikuliEvent class
    # http://doc.sikuli.org/region.html#SikuliEvent
    pass

class Region(SikuliClass):
    """ Manages interaction with Sikuli's Region """
    def find(self, PS):
        """
        Implements an interface for
            http://doc.sikuli.org/region.html#Region.find
        """
        return Match(self.obj.find(PS=PS))


    #TODO: Region class
    # http://doc.sikuli.org/region.html#Region
    pass

