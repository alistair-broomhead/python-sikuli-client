"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""

class RemoteLib(object):
    def __init__(self, remote):self.__lib = remote
    def __getattr__(self, name):
            if name in self.__lib.get_keyword_names():
                    def _(*args):return self.__lib.run_keyword(name, args)
                    _.__name__ = name
                    self.__dict__[name] = _
                    return _
            raise AttributeError()
class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    sikuliserver = None
    _
    def __init__(self,
                 host,
                 port=5637,
                 include=None,
                 exclude=None):
        from xmlrpclib import ServerProxy
        self.sikuliserver = ServerProxy("http://%s:%r"%(host, port))
