"""
Server-side classes
"""

from .sikuli_class import ServerSikuliClass


def _get_cls(cls_name):
    #noinspection PyUnresolvedReferences
    from sikuli import Sikuli

    class _cls(ServerSikuliClass):
        pass

    cls = dict(Sikuli.__dict__)[cls_name]
    _cls.__name__ = cls.__name__
    _cls.__doc__ = cls.__doc__
    _cls.__module__ = cls.__module__
    return _cls


class Vision(ServerSikuliClass):
    """
    Manages interaction with Sikuli's Vision:
        http://doc.sikuli.org/globals.html#Vision.setParameter
    """
    pass


SIKULI_CLASSES = {'Vision': Vision}
for key in ['App', 'Env', 'Finder', 'Match', 'Pattern', 'Region',
            'Screen', 'Settings', 'SikuliEvent']:
    exec 'SIKULI_CLASSES[key] = %s = _get_cls(key)'

del ServerSikuliClass
