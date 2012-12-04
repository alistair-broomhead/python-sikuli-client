"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""
from .finder import Finder
from .globals import Settings, App, Env, Vision
from .match import Match
from .pattern import Pattern
from .region import SikuliEvent, Region
from .screen import Screen

SIKULI_CLASSES = {v.__name__:v for v in
                  [Finder,
                   Settings, App, Env, Vision,
                   Match,
                   SikuliEvent, Region,
                   Screen]}
__ALL__ = sorted(list(SIKULI_CLASSES.keys()))
__author__ = 'Alistair Broomhead'

import json

KEYWORDS = {k: frozenset(v) for k, v in
            json.load(open("keywords.json")).items()}
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
