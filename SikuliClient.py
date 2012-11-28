"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""
import json
KEYWORDS = {
    k: frozenset(v) for k,v in
    json.load(open("keywords.json")).items()}
DEFAULT_EXPOSED = frozenset.union(
    KEYWORDS['APPS'],
    KEYWORDS['RGN_LOW_INPUT'],
    KEYWORDS['RGN_FIND'],
    KEYWORDS['RGN_INTERACT'])
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

#TODO: Settings class
# http://doc.sikuli.org/globals.html#Settings
#TODO: App class
# http://doc.sikuli.org/globals.html#App
#TODO: Other Env. Info
# http://doc.sikuli.org/globals.html#Env.getOS
#TODO: Tuning Vision Algorithm
# http://doc.sikuli.org/globals.html#Vision.setParameter
#TODO: Sikuli Events
# http://doc.sikuli.org/region.html#SikuliEvent
#TODO: Regions
# http://doc.sikuli.org/region.html#Region.click
#TODO: Screens
# http://doc.sikuli.org/screen.html#Screen.Screen
#TODO: Match Objects
# http://doc.sikuli.org/match.html#Match
#TODO: Finder
# http://doc.sikuli.org/finder.html
class SiculiUnreflected(object):
    """ Custom keyword handlers rather than those reflected over RPC """
    def _eval(self, jython_as_string):
        return self.remote.eval_jython(jython_as_string=jython_as_string)
    def __init__(self, remote):
        self.remote = remote
class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    sikuliserver = None
    def __init__(self,
                 host,
                 port=5637,
                 include=None,
                 exclude=None):
        include = frozenset(include) if include is not None else frozenset()
        exclude = frozenset(exclude) if exclude is not None else frozenset()
        from xmlrpclib import ServerProxy
        self._sikuliserver = RemoteLib(ServerProxy("http://%s:%r"%(host, port)))
        self._unreflected = SiculiUnreflected(self.sikuliserver)
        self._keywords = DEFAULT_EXPOSED.union(include).difference(exclude)
        for k in self._keywords:
            try:
                v = getattr(self._unreflected, k)
            except AttributeError:
                v = getattr(self._sikuliserver, k)
            self.__dict__[k] = v
