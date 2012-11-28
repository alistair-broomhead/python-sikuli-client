"""
Extra classes that implementent miscellaneous needed functionailty
"""
__author__ = 'Alistair Broomhead'

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
        self.remote = remote

    def _eval(self, jython_as_string):
        rv = self.remote.eval_jython(jython_as_string=jython_as_string)
        from . import SIKULI_CLASSES
        from .sikuli_class import SikuliClass
        if isinstance(rv, str):
            if len([name for name in SIKULI_CLASSES if rv.startswith(name)]):
                try:
                    return SikuliClass.from_string(rv)
                except BaseException:
                    pass
        return rv
