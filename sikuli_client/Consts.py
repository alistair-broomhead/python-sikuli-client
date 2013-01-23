"""

Constants from the server-side

.. toctree::
   :maxdepth: 2
   :glob:
"""
from .sikuli_class import ClientSikuliClass
from .misc import constructor


class Const(ClientSikuliClass):
    """ Constants """
    CONSTS = {}

    def __new__(cls, remote, server_id, *args, **kwargs):
        if not issubclass(cls, Const):
            TypeError("Expected Const")
        if server_id in cls.CONSTS:
            return cls.CONSTS[server_id]
        return super(Const, cls).__new__(cls, remote, server_id, *args,
                                         **kwargs)



@constructor(Const)
def _const_constructor(str_const):
    return str_const
