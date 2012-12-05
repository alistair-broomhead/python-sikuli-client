"""
SikuliClient is an XMLRPC client for SikuliServer - an instance of SikuliClient
should be held by each client-side instance of SikuliClass in order to allow it
to interact with the server-side class.
"""
__author__ = 'Alistair Broomhead'

import json
import os

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

class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    def _eval(self, jython_string):
        rv = self._sikuliserver.eval_jython(jython_string)
        if rv['status'] != 'PASS':
            print "\n\n", jython_string, '-->', rv['status'], ':\n\n', rv['traceback']
            assert rv['status'] == 'PASS'
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
        for k in self._keywords:
            try:
                v = getattr(self._unreflected, k)
            except AttributeError:
                v = getattr(self._sikuliserver, k)
            self.__dict__[k] = v
