""" Base class for types based on the Sikuli native types """
__author__ = 'Alistair Broomhead'
from sikuli_server.classes.sikuli_class import (SikuliClass,
                                                UnimplementedSikuliClass,
                                                SIKULI_OBJECTS)
class SikuliClass(SikuliClass):
    """ Base class for types based on the Sikuli native types """
    @property
    def _id(self):
        return self.remote_id
    def __new__(cls, remote, remote_id, *args, **kwargs):
        if remote_id in SIKULI_OBJECTS:
            kwargs['id_'] = remote_id
        return super(SikuliClass, cls).__new__(remote, remote_id, *args,**kwargs)

    def __init__(self, remote, remote_id, *args, **kwargs):
        """
        :type remote: SikuliServer
        """
        self.remote = remote
        self.remote_id = remote_id
