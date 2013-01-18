""" Base class for types based on the Sikuli native types """
__author__ = 'Alistair Broomhead'
SIKULI_OBJECTS = {}

class ServerSikuliClass(object):
    """ Base class for types based on the Sikuli native types """
    obj = None
    @property
    def _id(self): return id(self)
    def __new__(cls, obj=None, server_id=None, *args, **kwargs):
        """
        Obj is not used, however the signature has to be the same as __init__
        """
        if 'cls' in kwargs:
            try:
                from .. import classes
                cls = classes.__dict__[kwargs['cls']]
            except BaseException:
                pass
        if server_id is None:
            obj = type.__new__(cls, *args, **kwargs)
            SIKULI_OBJECTS[obj._id()] = obj
        elif not isinstance(SIKULI_OBJECTS[server_id], SikuliClass):
            raise TypeError(
                "%r is not an instance of %r" % (SIKULI_OBJECTS[server_id],
                                                 SikuliClass))
        else:
            obj = SIKULI_OBJECTS[server_id]
        obj.__dict__.update(kwargs)
        return obj
    def __init__(self, obj, *args, **kwargs):
        self.ojb = obj
    @property
    def _marshallable(self):
        return dict(cls=type(self).__name__,
                    id_=id(self))

class UnimplementedSikuliClass(ServerSikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r"%cls)

SikuliClass = ServerSikuliClass
#noinspection PyStatementEffect
"""
For convenience - anything importing
:class:`sikuli_client.sikuli_class.SikuliClass` will get
:class:`~sikuli_client.sikuli_class.ClientSikuliClass`, wheras anything
importing :class:`sikuli_server.class_definitions.sikuli_class.SikuliClass` will
get :class:`~sikuli_server.class_definitions.sikuli_class.ServerSikuliClass`
"""
