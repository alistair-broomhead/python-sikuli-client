"""
Jython script to run a robot remote library exposing the Sikuli API (and popen)
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
    def _new_jython_object(self, object_=None):
        id_ = self._next_id
        self._held_objects[id_] = object_
        self._next_id += 1
        return id_
    def _del_jython_object(self, id_):
        del self._held_objects[id_]
    def _get_jython_object(self, id_):
        return self._held_objects[id_]
    @property
    def _private_globals(self):
        if not hasattr(self, '__private_globals'):
            from classes import SIKULI_CLASSES
            self.__private_globals = SIKULI_CLASSES
        g = globals()
        g.update(self.__private_globals)
        return g
    def eval_jython(self, jython_as_string):
        """
        Gives a quick and dirty way to run jython directly on the SiculiServer -
        not intended for direct use, but for giving an interface for building a
        remote API
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
        from .class_definitions.sikuli_class import SikuliClass, UnimplementedSikuliClass
        if not isinstance(ret, SikuliClass):
            return RobotRemoteServer._handle_return_value(self, ret)
        elif isinstance(ret, UnimplementedSikuliClass):
            raise NotImplementedError("Not yet implemented this type")
        else:
            return ret._marshallable()

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
