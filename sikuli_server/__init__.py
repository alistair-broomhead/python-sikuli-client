"""
:mod:`sikuli_server`
========================================

Jython script to run a robot remote library exposing the Sikuli API (and popen)


.. toctree::
   :maxdepth: 2
   :glob:

   sikuli_server.classes
   sikuli_server.robotremoteserver
   sikuli_server.class_definitions
"""
try:
    #noinspection PyUnresolvedReferences
    from sikuli import Sikuli
except ImportError:
    pass


class SikuliServer(object):
    """
    Class into which to dump the namespace of sikuli.Sikuli
    """
    # Please don't use these directly
    def _new_jython_object(self, object_):
        if object_ is None:
            return object_
        id_ = self._next_id
        self._held_objects[id_] = [object_, 0]
        self._next_id += 1
        return id_

    def _gcollect(self):
        for id_ in (k for k, v in self._held_objects.items() if v[1] < 1):
            del self._held_objects[id_]

    def _del_jython_object(self, id_):
        self._held_objects[id_][1] -= 1
        self._gcollect()

    def _ref_jython_object(self, id_):
        self._held_objects[id_][1] += 1
        self._gcollect()

    def _get_jython_object(self, id_):
        return self._held_objects[id_][0]

    @property
    def _private_globals(self):
        if not hasattr(self, '__private_globals'):
            #from classes import SIKULI_CLASSES
            sd = dict(Sikuli.__dict__)

            def _get_cls(cls_name):
                from .class_definitions.sikuli_class import ServerSikuliClass

                class _cls(ServerSikuliClass):
                    pass
                cls = sd[cls_name]
                _cls.__name__ = cls.__name__
                _cls.__doc__ = cls.__doc__
                _cls.__module__ = cls.__module__
                return _cls
            self.__private_globals = {}
            for key in ['App', 'Env', 'Finder', 'Match', 'Pattern', 'Region',
                        'Screen', 'Settings', 'SikuliEvent']:
                self.__private_globals[key] = _get_cls(key)
            from .class_definitions.globals import Vision

            self.__private_globals['Vision'] = Vision
        g = globals()
        g.update(self.__private_globals)
        return g

    def eval_jython(self, jython_as_string):
        """
        Gives a quick and dirty way to run jython directly on the SiculiServer -
        not intended for direct use, but for giving an interface for building a
        remote API
        :param jython_as_string: str -- will be evaluated server-side
        """
        l = locals()
        return eval(jython_as_string, self._private_globals, l)

    def __init__(self):
        self.__dict__.update(Sikuli.__dict__)
        self._held_objects = {}
        self._next_id = 0


from robotremoteserver import RobotRemoteServer


class SikuliRobotRemoteServer(RobotRemoteServer):
    """ RemoteServer that deals with Sikuli types """
    def _handle_return_value(self, ret):
        from .class_definitions.sikuli_class import (ServerSikuliClass,
                                                     UnimplementedSikuliClass)
        if isinstance(ret, ServerSikuliClass):
            return ret._marshallable()
        else:
            return RobotRemoteServer._handle_return_value(self, ret)

    def __init__(self, port=5637, allow_stop=True):
        from socket import gethostname
        RobotRemoteServer.__init__(self,
                                   library=SikuliServer(),
                                   host=gethostname(),
                                   port=port,
                                   allow_stop=allow_stop)


def run_sikuli_server():
    """ runs the server """
    SikuliRobotRemoteServer(port=5637)

if __name__ == "__main__":
    run_sikuli_server()
