# coding=utf-8
"""
Client library for interacting with Siculi from Robotframework over XML-RPC
"""
f = lambda *x: frozenset(x)
# All of these sets of keywords are provided purely for convenience, as they can
# be unioned to give common feature-sets
#
# sets of keywords we get in the rf namespace by default
APPS = f('openApp', 'switchApp', 'closeApp', 'run', )
RGN_LOW_INPUT = f('mouseDown', 'mouseMove', 'mouseUp', 'wheel', 'keyDown',
                  'keyUp')
RGN_FIND = f('find', 'findAll', 'wait', 'waitVanish', 'exists')
RGN_INTERACT = f('click', 'doubleClick', 'rightClick', 'highlight', 'hover',
                 'dragDrop','drag', 'dropAt', 'type', 'paste')
# sets of keywords we don't by default get in the RF namespace
LOAD_JAR_FILE = f('load', )
SIKULI_SCRIPT = f('setShowActions', 'exit')
USER_INTERACTION = f('popup', 'input')
ENVIRONMENT = f('getImagePath', 'addImagePath', 'removeImagePath',
                'setBundlePath', 'getBundlePath')
RGN_ABSTRACT = f('getH', 'getW', 'getX', 'getY', 'setH', 'setW', 'setX', 'setY',
                 'moveTo', 'getROI', 'setROI', 'setRect', 'morphTo','getCenter',
                 'getTopLeft', 'getTopRight', 'getBottomLeft','getBottomRight',
                 'getScreen', 'getLastMatch','getLastMatches',
                 'setAutoWaitTimeout','getAutoWaitTimeout')
RGN_EXTENSION = f('offset', 'inside', 'nearby', 'above', 'below', 'left',
                     'right')
RGN_FIND_OBS = f('onAppear', 'onVanish', 'onChange', 'observe',
                         'observeInBackground', 'stopObserver')
RGN_OCR = f('text')
FINDFAILED = f('setFindFailedResponse', 'getFindFailedResponse',
               'setThrowException', 'getThrowException', )
RGN_DEPRECATED = f('getRegionFromPSRM', 'getLocationFromPSRML')
SCREEN = f('getNumberScreens', 'getBounds', 'capture', 'selectRegion')
del f
DEFAULT_EXPOSED = frozenset.union(
    APPS, RGN_LOW_INPUT, RGN_FIND, RGN_INTERACT)
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
