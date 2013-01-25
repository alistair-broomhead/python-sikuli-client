"""
Server-side classes
"""


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
from .sikuli_class import ServerSikuliClass


class Vision(ServerSikuliClass):
    """
    Manages interaction with Sikuli's Vision:
        http://doc.sikuli.org/globals.html#Vision.setParameter
    """
    pass
del ServerSikuliClass

SIKULI_CLASSES = dict
SIKULI_CLASSES['Vision'] = Vision
SIKULI_CLASSES['App'] = App = _get_cls('App')
SIKULI_CLASSES['Env'] = Env = _get_cls('Env')
SIKULI_CLASSES['Finder'] = Finder = _get_cls('Finder')
SIKULI_CLASSES['Match'] = Match = _get_cls('Match')
SIKULI_CLASSES['Pattern'] = Pattern = _get_cls('Pattern')
SIKULI_CLASSES['Region'] = Region = _get_cls('Region')
SIKULI_CLASSES['Screen'] = Screen = _get_cls('Screen')
SIKULI_CLASSES['Settings'] = Settings = _get_cls('Settings')
SIKULI_CLASSES['SikuliEvent'] = SikuliEvent = _get_cls('SikuliEvent')
