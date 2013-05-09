"""
SikuliClient is an XMLRPC client for SikuliServer - an instance of SikuliClient
should be held by each client-side instance of SikuliClass in order to allow it
to interact with the server-side class.
"""
from python_sikuli_client.exceptions import SikuliClientException

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


class SikuliClient(object):
    """
    Client for sikuliserver to expose a more limited set of keywords to rf
    """
    _session = None
    _garbage = []

    def Region(self, *args, **kwargs):
        """
        Create a new :class:`~region.Region` connected to this SikuliClient
        :param args: args to pass to :class:`~region.Region` contructor
        :param kwargs: kwargs to pass to :class:`~region.Region` contructor
        :rtype : SikuliServer.sikuli_client.Region
        """
        from python_sikuli_client.region import Region
        return Region.mknew(self, *args, **kwargs)

    def Location(self, *args, **kwargs):
        """
        Create a new :class:`~location.Location` connected to this SikuliClient
        :param args: args to pass to :class:`~location.Location` contructor
        :param kwargs: kwargs to pass to :class:`~location.Location` contructor
        :rtype : SikuliServer.sikuli_client.Location
        """
        from python_sikuli_client.location import Location

        return Location.mknew(self, *args, **kwargs)

    def Screen(self, *args, **kwargs):
        """
        Create a new :class:`~screen.Screen` connected to this SikuliClient
        :param args: args to pass to :class:`~screen.Screen` contructor
        :param kwargs: kwargs to pass to :class:`~screen.Screen` contructor
        :rtype : SikuliServer.sikuli_client.Screen
        """
        from python_sikuli_client.screen import Screen

        return Screen.mknew(self, *args, **kwargs)

    @property
    def screen_bounds(self):
        """ Get access to the bounds of the default screen """
        return self._eval('(lambda x: [x.x, x.y, x.width, x.height])'
                          '(Sikuli.SCREEN.getBounds())')

    @property
    def _current_pool(self):
        if self._session is None:
            return self._garbage
        return self._session

    @property
    def server_held_objects(self):
        """ Get the mapping of objects seen on the server """
        return self._sikuliserver.held_objects()['return']

    def _new_session(self):
        if self._session is None:
            self._session = []
            return True
        return False

    def _collect_session(self, was_not_in_session=True):
        if self._session is not None:
            for id_ in self._session:
                self._del_obj(id_)
            if was_not_in_session:
                self._session = None

    def _collect_garbage(self):
        for id_ in self._garbage:
            self._del_obj(id_)

    @property
    @contextlib.contextmanager
    def session(self):
        """
        All
        """
        was_not_in_session = self._new_session()
        with sikuli_client_session(**self._kwargs) as session:
            yield session
        self._collect_session(was_not_in_session)
        return

    def _del_obj(self, id_):
        self._sikuliserver.jython_object_addrefs(id_, -1)
        # self._eval('self._del_jython_object(%r)' % int(id_))
        # if self._session is not None and id_ in self._session:
        #     l = self._session
        # elif id_ in self._garbage:
        #     l = self._garbage
        # else:
        #     return
        # del l[l.index(id_)]
        # self._eval('self._gcollect()')

    def _add_obj(self, id_):
        self._sikuliserver.jython_object_addrefs(id_, 1)
        #self._eval('self._ref_jython_object(%r)' % int(id_))

    def _new_obj(self, id_):
        self._eval('self._new_jython_object(%r)' % int(id_))

    def _eval(self, jython_string):
        rv = self._sikuliserver.eval_jython(jython_string)
        if rv['status'] != 'PASS':
            ex = SikuliClientException(rv['error'] + '\n\n' + rv['traceback'])
            raise ex
        new_objects, ret = rv['return']
        self._current_pool.extend(new_objects)
        return ret

    def _eval_foreach(self, jython_string, args):
        rv = self._sikuliserver.eval_foreach(jython_string, args)
        if rv['status'] != 'PASS':
            ex = SikuliClientException(rv['error'] + '\n\n' + rv['traceback'])
            raise ex
        new_objects, ret = rv['return']
        self._current_pool.extend([x for x in new_objects
                                   if str(x) in self.server_held_objects])
        return ret

    def __init__(self,
                 host,
                 port=5637,
                 include=None,
                 exclude=None):
        include = frozenset(include) if include is not None else frozenset()
        exclude = frozenset(exclude) if exclude is not None else frozenset()
        from xmlrpclib import ServerProxy
        from python_sikuli_client.misc import RemoteLib, SikuliUnreflected
        self._kwargs = dict(host=host,
                            port=port,
                            include=include,
                            exclude=exclude)
        self._sikuliserver = RemoteLib(
            ServerProxy("http://%s:%r" % (host, port)))
        self._unreflected = SikuliUnreflected(self._sikuliserver)
        self._keywords = DEFAULT_EXPOSED.union(include).difference(exclude)
        self._garbage = []
        for k in self._keywords:
            try:
                v = getattr(self._unreflected, k)
            except AttributeError:
                v = getattr(self._sikuliserver, k)
            self.__dict__[k] = v

    def __del__(self):
        for id_ in self._garbage:
            self._del_obj(id_)

    def __clearall__(self):
        for id_, n in self.server_held_objects.items():
            for _ in range(n[1]):
                self._del_obj(int(id_))


#noinspection PyDocstring
@contextlib.contextmanager
def sikuli_client_session(host,
                          port=5637,
                          include=None,
                          exclude=None):
    """
    Creates a new SikuliClient for your session, making sure all server-side gc
    is performed on context exit
    """
    s = SikuliClient(host=host,
                     port=port,
                     include=include,
                     exclude=exclude)
    yield s
    for id_ in s._garbage:
        s._del_obj(id_)
    return

