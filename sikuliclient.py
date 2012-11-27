"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""

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
