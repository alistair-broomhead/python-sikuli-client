"""
SikuliClient is an XMLRPC client for SikuliServer - an instance of SikuliClient
should be held by each client-side instance of SikuliClass in order to allow it
to interact with the server-side class.
"""
__author__ = 'Alistair Broomhead'

import json
import os
import contextlib

JSON_FILENAME = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "keywords.json"
)

KEYWORDS = {k: frozenset(v) for k, v in
            json.load(open(JSON_FILENAME)).items()}
del json
DEFAULT_EXPOSED = frozenset.union(
    KEYWORDS['APPS'],
    KEYWORDS['RGN_LOW_INPUT'],
    KEYWORDS['RGN_FIND'],
    KEYWORDS['RGN_INTERACT'])


class SikuliClientException(Exception):
    """ Exception raised if SikuliClient cannot complete an _eval """
    pass


class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    _session = None
    _out_of_session = []

    @property
    @contextlib.contextmanager
    def session(self):
        """
        All
        """
        was_not_in_session = self._session is None
        if was_not_in_session:
            self._session = []
        yield self
        for id_ in self._session:
            self._del_obj(id_)
        if was_not_in_session:
            self._session = None
        return
#    def collect(self):
#        """
#        Does garbage collection
#        """
#        unmanaged = 0
#        import gc
#        gc.collect()
#        from .sikuli_class import ClientSikuliClass
#        while len(gc.garbage) - unmanaged > 0:
#            unmanaged = 0
#            managed = []
#            for i, obj in enumerate(gc.garbage):
#                if isinstance(obj, ClientSikuliClass):
#                    managed.append(i)
#                else:
#                    unmanaged += 1
#            for [i, obj] in ([i, gc.garbage[i]] for i in reversed(managed)):
#                if hasattr(obj, '__del__'):
#                    obj.__del__()
#                    del obj
#                    del gc.garbage[i]
#                else:
#                    print 'Undeletable', obj
#                    del obj
#                    del gc.garbage[i]
#
#            gc.collect()

    def _del_obj(self, id_):
        self._eval('self._del_jython_object(%r)' % int(id_))
        s = self._session
        o = self._out_of_session
        if s is not None and id_ in s:
            del s[s.index(id_)]
        elif id_ in o:
            del o[o.index(id_)]


    def _eval(self, jython_string):
#        self.collect()
        rv = self._sikuliserver.eval_jython(jython_string)
        if rv['status'] != 'PASS':
            ex = SikuliClientException(rv['error']+'\n\n'+rv['traceback'])
            raise ex
        return rv['return']

    def __init__(self,
                 host,
                 port=5637,
                 include=None,
                 exclude=None):
        include = frozenset(include) if include is not None else frozenset()
        exclude = frozenset(exclude) if exclude is not None else frozenset()
        from xmlrpclib import ServerProxy
        from .misc import RemoteLib, SikuliUnreflected

        self._sikuliserver = RemoteLib(
            ServerProxy("http://%s:%r" % (host, port)))
        self._unreflected = SikuliUnreflected(self._sikuliserver)
        self._keywords = DEFAULT_EXPOSED.union(include).difference(exclude)
        self._out_of_session = []
        for k in self._keywords:
            try:
                v = getattr(self._unreflected, k)
            except AttributeError:
                v = getattr(self._sikuliserver, k)
            self.__dict__[k] = v

    def __del__(self):
        for id_ in self._out_of_session:
            self._del_obj(id_)

    def __clearall__(self):
        for id_ in self._eval('self._held_objects'):
            self._del_obj(int(id_))
