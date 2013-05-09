"""
Exceptions for use in sikuli_client
"""
__author__ = 'Alistair Broomhead'


class SikuliClientException(Exception):
    """ Exception raised if SikuliClient cannot complete an _eval """
    pass


class FindFailed(SikuliClientException):
    """ Find operation failed """
    pass
