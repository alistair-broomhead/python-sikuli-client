""" Base class for types based on the Sikuli native types """
from functools import wraps
from sikuli_server.class_definitions.sikuli_class import (SikuliClass,
                                                          SIKULI_OBJECTS)
__author__ = 'Alistair Broomhead'
class SikuliClass(SikuliClass):
    """ Base class for types based on the Sikuli native types """
    _constructors = ()
    remote = None
    @staticmethod
    def run_on_remote(func):
        """
        Runs the decorated function but discards the result, so you can use it
        for sanity-checking but should not use it for actual processing, as
        this will be done on the server side.
        """
        @wraps(func)
        def _wrapper(self, *args):
            func(*args)
            return self.remote._eval("self._get_jython_object(%r).%s(%s)" % (
                self.server_id,
                func.__name__,
                ', '.join([repr(x) for x in args])))
        return _wrapper
    @staticmethod
    def run_modified_on_remote(func):
        """
        Runs the decorated function, setting the args of the wrapped function
        to the  result, so you can use it for sanity-checking but should not use
        it for actual processing, as this will be done on the server side.
        """
        @wraps(func)
        def _wrapper(self, *args, **kwargs):
            args = func(*args, **kwargs)
            return self.remote._eval("self._get_jython_object(%r).%s(%s)" % (
                self.server_id,
                func.__name__,
                ', '.join([repr(x) for x in args])))
        return _wrapper
    @classmethod
    def mknew(cls, remote, *args, **kwargs):
        """ Create a new object, instantiating it on the server side. """
        from .sikuli_client import SikuliClient
        assert isinstance(remote, SikuliClient)
        _remote, cls.remote = cls.remote, remote
        for method in cls._constructors:
            try:
                server_id = method(*args, **kwargs)
            except BaseException, e:
                print e
                continue
            else:
                if isinstance(_remote, SikuliClient): cls.remote = _remote
                #from pdb import set_trace; set_trace()
                return cls(remote=remote, server_id=server_id)
        raise NotImplementedError(
            "Not created a constructor for args=%r kwargs=%r" % (args, kwargs))
    @property
    def _id(self):
        return self.server_id
    def __new__(cls, remote, server_id, *args, **kwargs):
        cls.remote = remote
        if server_id in SIKULI_OBJECTS:
            kwargs['server_id'] = server_id
        return object.__new__(cls, remote, *args, **kwargs)

    def __init__(self, remote, server_id, *args, **kwargs):
        """
        :type server_id: int
        :type remote: SikuliClient
        """
        self.remote = remote
        self.server_id = server_id
class UnimplementedSikuliClass(SikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r" % cls)