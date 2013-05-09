"""
Extra classes that implementent miscellaneous needed functionailty
"""
from functools import wraps
from python_sikuli_client.sikuli_class import ClientSikuliClass

__author__ = 'Alistair Broomhead'
from python_sikuli_client.pattern import Pattern
from python_sikuli_client.match import Match


class RemoteLib(object):
    """ Re-exposes a classes keywords wrapped by robotremotelibrary.py """

    def __init__(self, remote):
        self.__lib = remote

    def __getattr__(self, name):
        if name in self.__lib.get_keyword_names():
            def _(*args):
                return self.__lib.run_keyword(name, args)

            _.__name__ = name
            self.__dict__[name] = _
            return _
        raise AttributeError()


class SikuliUnreflected(object):
    """ Custom keyword handlers rather than those reflected over RPC """

    def __init__(self, remote):
        """
        :type remote: SikuliServer
        """
        self.remote = remote

    def find(self, PS):
        """

        :param PS: :class:`~python_sikuli_client.pattern.Pattern` or str
        :rtype: :class:`~python_sikuli_client.match.Match`

        Find a particular GUI element, which is seen as the given image or
        just plain text. The given file name of an image specifies the
        element's appearance. It searches within the region and returns the best
        match, which shows a similarity greater than the minimum similarity
        given by the pattern. If no similarity was set for the pattern by
        :meth:`python_sikuli_client.pattern.Pattern.similar` before, a default minimum
        similarity of 0.7 is set automatically.

        If autoWaitTimeout is set to a non-zero value, find() just acts as a
        wait().

        **Side Effect** *lastMatch*: the best match can be accessed using
        :meth:`~python_sikuli_client.region.Region.getLastMatch` afterwards.
        """
        if isinstance(PS, Pattern):
            assert isinstance(PS, Pattern)
            ps = "self._get_jython_object(%r)" % PS.remote_id
        else:
            ps = repr(PS)
        #noinspection PyUnresolvedReferences
        match_id = self._eval("self._new_jython_object(self.find(%s))" % ps)
        # noinspection PyArgumentList
        return Match(remote=self.remote, id_=match_id)


def dropNones(num_required, keys, *args, **kwargs):
    """
    Was finding this repoetitive.
    :param num_required: how many args are required in total
    :param keys: dict of keys and (bool) is_required (None ignores this)
    :param args:
    :param kwargs: some of these will not
    """
    if keys is None:
        kw = {k: v for k, v in kwargs.items() if v is not None}
    else:
        kw = {k: v for k, v in kwargs.items()
              if (v is not None) or (k in keys and keys[k])}
    while len(kw) + len(args) > num_required and args[-1] is None:
        args = args[:-1]
    return args, kw


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


def return_from_remote(rtype):
    """
    Decorator factory returning a run_on_remote decorator which marshals and
    unmarshals the return type as ``rtype`` where ``rtype`` must be either a
    subclass of :class:`ClientSikuliClass`, or the string name of a
    class in :mod:`~python_sikuli_client.classes`

    :param rtype: return type

    .. code-block:: python

        @return_from_remote(rtype)
        def func(*args, **kwargs):
            ...
    """

    def _new_decorator(func):
        func = run_on_remote(func)
        rt = []

        # noinspection PyUnusedLocal
        @func.func
        def _inner_func(self, *args, **kwargs):
            location_id = self.remote._eval(
                "self._new_jython_object("
                "   self._get_jython_object(%r).%s(%s))" % (
                    self._id,
                    func.__name__,
                    ', '.join([s_repr(x) for x in args])))
            if not rt:
                from python_sikuli_client.classes import SIKULI_CLASSES

                cls = (rtype if isinstance(rtype, ClientSikuliClass) else
                       SIKULI_CLASSES[rtype])
                rt.append(cls)
            else:
                cls = rt[0]
            obj = cls(remote=self.remote, server_id=str(location_id))
            #obj.remote._del_obj(location_id)
            return obj

        return func

    return _new_decorator


def DEFERRED(func):
    """
    Decorator for unimplemented interfaces
    :type func: function
    """
    func.__doc__ = """ .. todo:: Implement %r (later) """ % func.__name__
    return func


def TODO(func):
    """
    Decorator for unimplemented interfaces
    :type func: function
    """
    func.__doc__ = """ .. todo:: Implement %r (soon) """ % func.__name__
    return func


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
        if not self._on_server:
            raise NameError('%r has been garbage collected on the server side'
                            % self)
        func(self, *args, **kwargs)
        if "arg" in func._augment:
            arg_kw = func._augment["arg"](self, *args, **kwargs)
            if len(arg_kw) == 2 and (isinstance(arg_kw[0], tuple) and
                                     isinstance(arg_kw[1], dict)):
                args, kwargs = arg_kw
            else:
                args, kwargs = arg_kw, {}
        result = func._augment['inner'](self, *args, **kwargs)
        if "post" in func._augment:
            return func._augment["post"](self, result)
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

    func.arg = _arg
    func.post = _post
    func.func = _func
    func.run = _outer
    return func


def s_repr(obj):
    """
    :param obj: object
    """
    return (repr(obj) if not isinstance(obj, ClientSikuliClass) else
            obj._str_get)
