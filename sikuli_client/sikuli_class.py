""" Base class for types based on the Sikuli native types """
from . import SikuliClient
from sikuli_server.classes.sikuli_class import (SikuliClass,
                                                SIKULI_OBJECTS)
__author__ = 'Alistair Broomhead'
class SikuliClass(SikuliClass):
    """ Base class for types based on the Sikuli native types """
    _contructors = ()
    remote = None
    @classmethod
    def mknew(cls, remote, *args, **kwargs):
        """ Create a new object, instantiating it on the server side. """
        assert isinstance(remote, SikuliClient)
        _remote, cls.remote = cls.remote, remote
        for method in cls._contructors:
            try:
                remote_id = method(*args, **kwargs)
            except BaseException:
                continue
            else:
                if isinstance(_remote, SikuliClient): cls.remote = _remote
                return cls(remote=remote, id_=remote_id)
        raise NotImplementedError(
            "Not created a constructor for args=%r kwargs=%r" % (args, kwargs))
    @property
    def _id(self):
        return self.remote_id
    def __new__(cls, remote, remote_id, *args, **kwargs):
        cls.remote = remote
        if remote_id in SIKULI_OBJECTS:
            kwargs['id_'] = remote_id
        return super(SikuliClass, cls).__new__(remote, remote_id, *args,**kwargs)

    def __init__(self, remote, id_, *args, **kwargs):
        """
        :type id_: int
        :type remote: SikuliClient
        """
        self.remote = remote
        self.remote_id = id_
class UnimplementedSikuliClass(SikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r" % cls)
