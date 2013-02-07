"""
Base class for types based on the Sikuli native types
"""
from functools import wraps
from SikuliServer.sikuli_server.sikuli_class import (ServerSikuliClass,
                                                     SIKULI_OBJECTS)

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
            except TypeError as e:
                print e
                continue
            else:
                if isinstance(_remote, SikuliClient):
                    cls.remote = _remote
                obj = cls(remote=remote, server_id=server_id, is_new=True)
                obj.remote._del_obj(server_id)
                return obj
        raise NotImplementedError(
            "Not created a constructor for args=%r kwargs=%r" % (args, kwargs))

    @property
    def _id(self):
        return self.server_id

    @property
    def _str_get(self):
        return "self._get_jython_object(%r)" % self.server_id

    @property
    def _on_server(self):
        if not int(self._id) in (int(id_)
                                 for id_ in self.remote.server_held_objects):
            return False
        return True

    def __new__(cls, remote, server_id, *args, **kwargs):
        cls.remote = remote
        obj = object.__new__(cls, remote, *args, **kwargs)
        return obj

    #noinspection PyUnusedLocal
    def __init__(self, remote, server_id, is_new=False, *args, **kwargs):
        """
        :type server_id: int
        :type remote: SikuliClient
        """
        super(ClientSikuliClass, self).__init__(None)

        def _apply_key(key):
            try:
                func = getattr(self, key)
                if func._augment is None:
                    raise AttributeError
                runner = func.run
            except AttributeError:
                return

            @wraps(func)
            def _outer(*args, **kwargs):
                return runner(self, *args, **kwargs)

            setattr(self, key, _outer)

        for key in dir(self):
            _apply_key(key)

        self.remote = remote
        self.server_id = server_id
        self.remote._add_obj(server_id)
        if not is_new:
            self.remote._current_pool.append(server_id)


#noinspection PyArgumentList
class UnimplementedSikuliClass(ClientSikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r" % cls)


SikuliClass = ClientSikuliClass
#noinspection PyStatementEffect
"""
For convenience - anything importing
:class:`sikuli_client.sikuli_class.SikuliClass` will get
:class:`~sikuli_client.sikuli_class.ClientSikuliClass`, wheras anything
importing :class:`sikuli_server.class_definitions.sikuli_class.SikuliClass` will
get :class:`~sikuli_server.class_definitions.sikuli_class.ServerSikuliClass`
"""
