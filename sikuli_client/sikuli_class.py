""" Base class for types based on the Sikuli native types """
from functools import wraps
from sikuli_server.class_definitions.sikuli_class import (ServerSikuliClass,
                                                          SIKULI_OBJECTS)
__author__ = 'Alistair Broomhead'
class ClientSikuliClass(ServerSikuliClass):
    """ Base class for types based on the Sikuli native types """
    _constructors = ()
    _remote_funcs = {}
    remote = None
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
    @property
    def _str_get(self):
        return "self._get_jython_object(%r)"%self.server_id
    def __new__(cls, remote, server_id, *args, **kwargs):
        from .sikuli_client import SikuliClient
        assert isinstance(remote, SikuliClient)
        cls.remote = remote
        if server_id in SIKULI_OBJECTS:
            kwargs['server_id'] = server_id
        return object.__new__(cls, remote, *args, **kwargs)

    def __init__(self, remote, server_id, *args, **kwargs):
        """
        :type server_id: int
        :type remote: SikuliClient
        """
        super(ClientSikuliClass, self).__init__(None)
        self.remote = remote
        self.server_id = server_id

class UnimplementedSikuliClass(ClientSikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r" % cls)


def run_on_remote(func):
    """
    Runs the decorated function but discards the result, so you can use it
    for sanity-checking but should not use it for actual processing, as
    this will be done on the server side.

    The decorated function can have a number of properties that modify the
    way it is run, each of which should be a function itself:

        func.arg(*args, **kwargs):
            The output of this will be used as args for the inner wrapper
        func.post(result):
            This takes the output of the inner wrapper, and its ouput is
            returned by the outer wrapper
        func.func(*args, **kwargs):
            Replaces the default inner function - should handle all interaction
            with the server
    """
    def _inner(self, *args):
        return self.remote._eval("self._get_jython_object(%r).%s(%s)" % (
            self._id,
            func.__name__,
            ', '.join([repr(x) for x in args])))

    func.func = _inner
    @wraps(func)
    def _outer(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if hasattr(func, "arg"):
            args, kwargs = func.arg(*args, **kwargs), {}
        result = func.func(*args, **kwargs)
        if hasattr(func, "post"):
            return func.post(result)
        else:
            return result
    def _arg(arg_func):
        func.arg = arg_func
        return _outer
    def _post(post_func):
        func.post = post_func
        return _outer
    def _func(func_func):
        func.func = func_func
        return _outer
    _outer.arg = _arg
    _outer.post = _post
    _outer.func = _func
    return _outer

def constructor(cls):
    """
    Usage:
        @constructor(cls)
        def func(*args, **kwargs):
        ...
    Uses func as a potential constructor for cls:
    func should return the string which when evaluated by jython gives the
    object we want.
    """
    def _wrapper(func):
        @wraps(func)
        def _func(*args, **kwargs):
            return cls.remote._eval("self._new_jython_object(%s)" %
                                    func(*args, **kwargs))

        cls._constructors = cls._constructors + (_func,)
        return _func
    return _wrapper

SikuliClass = ClientSikuliClass
