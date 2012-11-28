""" Base class for types based on the Sikuli native types """
__author__ = 'Alistair Broomhead'

class SikuliClass(object):
    """ Base class for types based on the Sikuli native types """
    @staticmethod
    def from_string(instance_as_string):
        """ Initialises the correct class to unmarshal this string """


class UnimplementedSikuliClass(SikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
