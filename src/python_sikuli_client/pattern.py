"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/pattern.html
"""
__author__ = 'Alistair Broomhead'
from python_sikuli_client.sikuli_class import UnimplementedSikuliClass


class Pattern(UnimplementedSikuliClass):
    """ Manages interaction with Sikuli's Pattern """

    def __init__(self, remote, server_id, is_new=False, *args, **kwargs):
        # noinspection PyArgumentList
        super(Pattern, self).__init__(remote, server_id, is_new=False, *args,
                                      **kwargs)
        self.remote_id = None
        self.is_new = is_new

    #TODO: Finder
    # http://doc.sikuli.org/pattern.html#Pattern
    pass
