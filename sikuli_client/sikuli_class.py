"""
Base class for types based on the Sikuli native types
"""
from functools import wraps
try:
    from ..sikuli_server.class_definitions.sikuli_class import (
        ServerSikuliClass, SIKULI_OBJECTS)
except ValueError:
    from SikuliServer.sikuli_server.class_definitions.sikuli_class import (
        ServerSikuliClass, SIKULI_OBJECTS)

__author__ = 'Alistair Broomhead'


class ClientSikuliClass(ServerSikuliClass):
    """ Base class for types based on the Sikuli native types """
    _constructors = ()
    _remote_funcs = {}
    remote = None

    #noinspection PyDocstring
    @classmethod
    def mknew(cls, remote, *args, **kwargs):
        """ Create a new object, instantiating it on the server side. """
        from .sikuli_client import SikuliClient

        assert isinstance(remote, SikuliClient)
        _remote, cls.remote = cls.remote, remote
        for method in cls._constructors:
            try:
                server_id = method(*args, **kwargs)
            except BaseException as e:
                print(e)
                continue
            else:
                if isinstance(_remote, SikuliClient):
                    cls.remote = _remote
                    #from pdb import set_trace; set_trace()
                return cls(remote=remote, server_id=server_id)
        raise NotImplementedError(
            "Not created a constructor for args=%r kwargs=%r" % (args, kwargs))

    @property
    def _id(self):
        return self.server_id

    @property
    def _str_get(self):
        return "self._get_jython_object(%r)" % self.server_id

    def __new__(cls, remote, server_id, *args, **kwargs):
        from .sikuli_client import SikuliClient

        assert isinstance(remote, SikuliClient)
        cls.remote = remote
        if server_id in SIKULI_OBJECTS:
            kwargs['server_id'] = server_id
            #noinspection PyArgumentList
        return object.__new__(cls, remote, *args, **kwargs)

    #noinspection PyUnusedLocal
    def __init__(self, remote, server_id, *args, **kwargs):
        """
        :type server_id: int
        :type remote: SikuliClient
        """
        super(ClientSikuliClass, self).__init__(None)
        for key in dir(self):
            try:
                func = getattr(self, key)
            except AttributeError:
                pass
            else:
                try:
                    from functools import partial, wraps
                    run = wraps(func.run)(partial(func.run, self))
                    setattr(self, key, run)
                except AttributeError:
                    pass
        self.remote = remote
        self.server_id = server_id


class UnimplementedSikuliClass(ClientSikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r" % cls)


def s_repr(obj):
    """ :param obj: object """
    return (repr(obj) if not isinstance(obj, SikuliClass)
            else "self._get_jython_object(%r)" % obj._str_get)


def run_on_remote(func):
    """
    :param func: function to decorate

    Runs the decorated function but discards the result, so you can use it
    for sanity-checking but should not use it for actual processing, as
    this will be done on the server side.

    The decorated function can have a number of properties that modify the
    way it is run, each of which should be a function itself:

        ``func.arg(*args, **kwargs)``:
            The output of this will be used as args for the inner wrapper
        ``func.post(result)``:
            This takes the output of the inner wrapper, and its ouput is
            returned by the outer wrapper
        ``func.func(*args, **kwargs)``:
            Replaces the default inner function - should handle all interaction
            with the server

    .. code-block:: python

        @run_on_remote
        def func(*args, **kwargs):
            ...
    """
    gjo = "self._get_jython_object"
    func._augment = {
        'inner': lambda self, *args: (self.remote._eval("%s(%r).%s(%s)"
                                      % (gjo, self._id, func.__name__,
                                         ', '.join([s_repr(x)for x in args]))))
    }

    @wraps(func)
    def _outer(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if "arg" in func._augment:
            args, kwargs = func._augment["arg"](self, *args, **kwargs), {}
        result = func._augment['inner'](self, *args, **kwargs)
        if "post" in func._augment:
            return func.post(result)
        else:
            return result

    def _arg(arg_func):
        func._augment['arg'] = arg_func
        return func

    def _post(post_func):
        func._augment['post'] = post_func
        return func

    def _func(func_func):
        func._augment['inner'] = func_func
        return func

    func.arg  = _outer.arg = _arg
    func.post = _outer.post = _post
    func.func = _outer.func = _func
    func.run  = _outer.run = _outer
    return func


def TODO(func):
    """
    Decorator for unimplemented interfaces
    :type func: function
    """
    func.__doc__ = """ .. todo:: Implement %r (soon) """ % func
    return func


def DEFERRED(func):
    """
    Decorator for unimplemented interfaces
    :type func: function
    """
    func.__doc__ = """ .. todo:: Implement %r (later) """ % func
    return func


def return_from_remote(rtype):
    """
    Decorator factory returning a run_on_remote decorator which marshals and
    unmarshals the return type as ``rtype`` where ``rtype`` must be either a
    subclass of :class:`ClientSikuliClass`, or the string name of a
    class in :mod:`~sikuli_client.classes`

    :param rtype: return type

    .. code-block:: python

        @return_from_remote(rtype)
        def func(*args, **kwargs):
            ...
    """
    rt = []

    def _new_decorator(func):
        decorated = run_on_remote(func)

        @wraps(func)
        def _inner(self, *args):
            location_id = self.remote._eval(
                "self._new_jython_object("
                "   self._get_jython_object(%r).%s(%s))" % (
                    self._id,
                    func.__name__,
                    ', '.join([s_repr(x) for x in args])))
            if not rt:
                from .classes import SIKULI_CLASSES

                rt.append(rtype
                          if isinstance(rtype, ClientSikuliClass) else
                          SIKULI_CLASSES[rtype])
            return rt[0](remote=self.remote, server_id=location_id)

        decorated._augment['inner'] = _inner
        return decorated

    return _new_decorator


def constructor(cls):
    """
    :param cls: class to use decorated function as constructor for

    Uses func as a potential constructor for cls:
    func should return the string which when evaluated by jython gives the
    object we want.

    .. code-block:: python

        @constructor(cls)
        def func(*args, **kwargs):
            ...
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
#noinspection PyStatementEffect
"""
For convenience - anything importing
:class:`sikuli_client.sikuli_class.SikuliClass` will get
:class:`~sikuli_client.sikuli_class.ClientSikuliClass`, wheras anything
importing :class:`sikuli_server.class_definitions.sikuli_class.SikuliClass` will
get :class:`~sikuli_server.class_definitions.sikuli_class.ServerSikuliClass`
"""
