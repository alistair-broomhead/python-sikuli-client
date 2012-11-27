"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""

class RemoteLib(object):
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

class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    sikuliserver = None
    _defaults = ("click",
                 "")
    def __init__(self,
                 host,
                 port=5637,
                 include=None,
                 exclude=None):
        if include is None: include = []
        if exclude is None: exclude = []
        from xmlrpclib import ServerProxy
        self.sikuliserver = RemoteLib(ServerProxy("http://%s:%r"%(host, port)))
        self._keywords = []
        self._keywords.extend([x for x in self._defaults if x not in exclude])
        self._keywords.extend([x for x in include        if x not in exclude])
        for keyword in self._keywords:
            self.__dict__[keyword] = getattr(self.sikuliserver, keyword)


