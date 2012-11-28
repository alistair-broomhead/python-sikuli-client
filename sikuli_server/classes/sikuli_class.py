""" Base class for types based on the Sikuli native types """
__author__ = 'Alistair Broomhead'
SIKULI_OBJECTS = {}
class SikuliClass(object):
    """ Base class for types based on the Sikuli native types """
    @property
    def _id(self):
        return id(self)
    def __new__(cls, id_=None, *args, **kwargs):
        from .import SIKULI_CLASSES
        if 'cls' in kwargs and cls in SIKULI_CLASSES:
            cls = SIKULI_CLASSES[kwargs['cls']]
        if id_ is None:
            obj = type.__new__(cls, *args, **kwargs)
            SIKULI_OBJECTS[obj._id()] = obj
        elif not isinstance(SIKULI_OBJECTS[id_], cls):
            raise TypeError(
                "%r is not an instance of %r"%(SIKULI_OBJECTS[id_], cls))
        else:
            obj = SIKULI_OBJECTS[id_]
        obj.__dict__.update(kwargs)
        return obj
    @property
    def _marshallable(self):
        return dict(cls=type(self).__name__,
                    id_=id(self))


class UnimplementedSikuliClass(SikuliClass):
    """ Base class for unimplemented types based on the Sikuli native types """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Not implemented %r"%cls)

