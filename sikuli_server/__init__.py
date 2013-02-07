"""
:mod:`sikuli_server`
========================================

Jython script to run a robot remote library exposing the Sikuli API (and popen)


.. toctree::
   :maxdepth: 2
   :glob:

   sikuli_server.classes
   sikuli_server.robotremoteserver
   sikuli_server.sikuli_class
"""

try:
    #noinspection PyUnresolvedReferences
    from sikuli import Sikuli
except ImportError:
    pass

from os.path import abspath
lfn = abspath("./log.txt")
from threading import Lock
lfn_l = Lock()


def _writelog(txt):
    from sys import stderr
    lfn_l.acquire()
    logfile = open(lfn, "a")
    o = '%s\n%s\n' % (txt, '-' * 80)
    logfile.write(o)
    stderr.write(o)
    while not logfile.closed:
        logfile.close()
    lfn_l.release()
logfile = open(lfn, "w")
logfile.write('')
while not logfile.closed:
    logfile.close()


class SikuliServer(object):
    """
    Class into which to dump the namespace of sikuli.Sikuli
    """

    def _id(self):
        i = 0
        while True:
            yield i
            i += 1

    # Please don't use these directly
    def _new_jython_object(self, object_):
        if object_ is None:
            return object_
        id_ = self._id.next()
        self._held_objects[id_] = [object_, 1]
        self._eval_objects.append(id_)
        return id_

    def _gcollect(self):
        for id_ in (int(k) for k, v in self._held_objects.items() if v[1] < 1):
            del self._held_objects[id_]

    def _del_jython_object(self, id_):
        id_ = int(id_)
        if id_ in self._held_objects:
            self._held_objects[id_][1] -= 1

    def _ref_jython_object(self, id_):
        id_ = int(id_)
        self._held_objects[id_][1] += 1

    def _get_jython_object(self, id_):
        return self._held_objects[int(id_)][0]

    @property
    def held_objects(self):
        """ Copy of the map of held objects """
        return self._held_objects.copy()

    @property
    def _private_globals(self):
        if not hasattr(self, '__private_globals'):
            from .classes import SIKULI_CLASSES

            self.__private_globals = {}
            self.__private_globals.update(SIKULI_CLASSES)
        g = dict(globals()).copy()
        g.update(self.__private_globals)
        return g

    def min_similar(self, sim):
        Sikuli.Settings.MinSimilarity = sim

    def eval_jython(self, jython_as_string):
        """
        Gives a quick and dirty way to run jython directly on the SiculiServer -
        not intended for direct use, but for giving an interface for building a
        remote API
        :param jython_as_string: str -- will be evaluated server-side
        """
        l = locals()
        old_eval = self._eval_objects
        self._eval_objects = []
        _ = '\n%s\n' % ('-' * 80)
        txt = '%sEvaluated %r%s' % (_, jython_as_string, _)
        try:
            ret = eval(jython_as_string, self._private_globals, l)
            _writelog('%sReturned %r' % (txt, ret))
        except BaseException, e:
            _writelog('%sException %r' % (txt, e))
            raise e
        new_eval, self._eval_objects = self._eval_objects, old_eval
        return new_eval, ret

    def eval_foreach(self, jython_as_string, args):
        """
        Gives a quick and dirty way to run jython directly on the SiculiServer -
        not intended for direct use, but for giving an interface for building a
        remote API. Exceptions will be returned as a string.

        :param jython_as_string: str -- will be evaluated server-side
        :param args: iterable of things to have in the local namspace as 'arg'
        """
        l = locals().copy()
        old_eval = self._eval_objects
        self._eval_objects = []
        from threading import Thread, Lock

        ret_l = Lock()
        ret = dict()

        def _e(i, arg):
            ret_l.acquire()
            ret[(i, arg)] = None
            ret_l.release()
            l_ = l.copy()
            l_['arg'] = arg

            txt = ('\n%s\n[%r] Evaluated %r with arg as %r\n%s\n'
                   % ('-' * 80, i, jython_as_string, arg, '-' * 80))
            try:
                r = eval(jython_as_string, self._private_globals, l_)
                _writelog('%s[%r] Returned %r' % (txt, i, r))
            except BaseException, r:
                _writelog('%s[%r] Exception %r' % (txt, i, r))
            ret_l.acquire()
            ret[(i, arg)] = r
            ret_l.release()

        threads = [Thread(target=_e, args=(i, arg,)) for i, arg in
                   enumerate(args)]
        start_thread = lambda t: t.start()
        join_thread = lambda t: t.join()
        map(start_thread, threads)
        map(join_thread, threads)
        new_eval, self._eval_objects = self._eval_objects, old_eval
        return new_eval, ret

    def __init__(self):
        self.__dict__.update(Sikuli.__dict__)
        self._held_objects = {}
        self._id = type(self)._id(self)
        self._eval_objects = []


from robotremoteserver import RobotRemoteServer


class SikuliRobotRemoteServer(RobotRemoteServer):
    """ RemoteServer that deals with Sikuli types """

    def _handle_return_value(self, ret):
        from .sikuli_class import (ServerSikuliClass, UnimplementedSikuliClass)

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
